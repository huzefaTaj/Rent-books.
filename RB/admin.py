from django.contrib import admin
from .models import Book, Rental
from dateutil.relativedelta import relativedelta  # Import it here
from datetime import date

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'page_count']

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'start_date', 'end_date', 'fee')
