from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Rental
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from datetime import date
from datetime import datetime, timedelta

def index(request):
    # Fetch all books and rentals
    books = Book.objects.all()
    rentals = Rental.objects.all()

    return render(request, 'index.html', {'books': books, 'rentals': rentals})

def prolong_rental(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    
    # Prolong the end date by one month (30 days)
    rental.end_date += timedelta(days=30)

    # Calculate the total rental period in months
    total_months = (rental.end_date - rental.start_date).days // 30  # Total months
    if total_months > 1:  # Only charge if rental period exceeds free month
        rental.fee = calculate_fee(rental.book) * (total_months - 1)  # Fee for months beyond the free month

    rental.save()
    return redirect('index') 

def calculate_fee(book):
    # Calculate the fee based on the page count
    page_count = book.page_count or book.page_count_median
    return page_count / 100

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Create a new user
        user = User.objects.create(
            username=username,
            password=make_password(password),  # Hash the password
            email=email,
        )
        user.save()
        link = f"<a href='/'> Go to Dashboard</a>"
        return HttpResponse(f"User '{username}' created successfully! {link}")

    return render(request, 'create_user.html')
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        # Create the book object (page count will be fetched from the OpenLibrary API)
        book = Book.objects.create(title=title, author=author)
        link = f"<a href='/'> Go to Dashboard</a>"
        
        return HttpResponse(f"Book '{book.title}' by {book.author} created successfully! {link}")

    return render(request, 'create_book.html')

def create_rental(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        end_date_str = request.POST.get('end_date')

        user = get_object_or_404(User, id=user_id)
        book = get_object_or_404(Book, id=book_id)

        # Convert the end date string from the form to a date object
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        start_date = datetime.now().date()

        # Calculate the rental fee
        fee = 0
        if end_date > start_date + timedelta(days=30):  # If more than a month
            fee = calculate_fee(book)

        # Create a new rental
        rental = Rental.objects.create(user=user, book=book, start_date=start_date, end_date=end_date, fee=fee)
        link = f"<a href='/'> Go to Dashboard</a>"

        return HttpResponse(f"Rental created for {user.username} with book '{book.title}' until {rental.end_date}. Fee: ${rental.fee:.2f} {link}")

    users = User.objects.all()
    books = Book.objects.all()
    return render(request, 'create_rental.html', {'users': users, 'books': books})

