from django.contrib.auth.models import User
from django.db import models
import requests
from dateutil.relativedelta import relativedelta  # Import it here

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    page_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.page_count:
            self.fetch_page_count()
        super().save(*args, **kwargs)

    def fetch_page_count(self):
        url = f'https://openlibrary.org/search.json?title={self.title}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['docs']:
                self.page_count = data['docs'][0].get('number_of_pages', 
                                      data['docs'][0].get('number_of_pages_median', 0))

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
