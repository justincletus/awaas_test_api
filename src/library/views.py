import os
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required

from django.http import Http404, HttpResponse
from django.contrib.sessions.models import Session
from django.utils import timezone
from pprint import pprint
from .models import Book, BookCategory, BookInstance, Author
import boto3
from botocore.exceptions import ClientError
# from .djreservation.views import ProductReservationView
# from djreservation.views import ProductReservationView
from djreservation.views import ProductReservationView

from core.models import Profile

from django.contrib.auth.models import User
from library.forms import BookInstanceForm
from datetime import datetime, timedelta


# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail


# from django_datatables_view.base_datatable_view import BaseDatatableView


# Create your views here.

from django.views import generic

# class BookListView(generic.ListView):
#     model = Book
#     paginate_by = 10

# class BookDetailView(generic.DetailView):
#     model = Book

# class AuthorListView(generic.ListView):
#     model = Author
#     paginate_by = 10

# class AuthorDetailView(generic.DetailView):
#     model = Author

def book_list_view(request):
    queryset = Book.objects.all()
    num_books = Book.objects.all().count()
    num_book_instances = BookInstance.objects.all().count()

    #available copies of book
    num_book_instance_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    #number of visits to this view.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    context = {
        'book_list': queryset,
        'num_books': num_books,
        'num_book_instances': num_book_instances,
        'num_book_instance_available': num_book_instance_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, "library/book_list.html", context)

def book_detail_view(request, id):
    obj = get_object_or_404(Book, id=id)

    context = {
        "book": obj
    }

    return render(request, "library/book_detail.html", context)

def author_list_view(request):
    queryset = Author.objects.all()

    context = {
        'author_list': queryset
    }

    return render(request, "library/authors_list.html", context)

def author_detail_view(request, id):
    obj = get_object_or_404(Author, id=id)

    context = {
        "author": obj
    }

    return render(request, "library/author_detail.html", context)

def book_search_view(request):
    queryset = Book.objects.all()

    # context = []
    # context['book_list'] = array(queryset)

    #available copies of book
    book_instance_available = BookInstance.objects.filter(status__exact='a')

    context = {
        "book_list": queryset,
        "book_instance_available": book_instance_available
    }

    return render(request, "library/book_search.html", context)

@login_required
def user_account_detail(request):
    current_user = request.user

    base_model = BookInstance
    paginate_by = 5

    Bookinstance_details = BookInstance.objects.filter(borrower=request.user).values('book_id').get()
    
    book_detail = Book.objects.filter(id=Bookinstance_details['book_id']).get()
    
    user_object = BookInstance.objects.filter(borrower=request.user).filter(status__exact='r').order_by('due_back')
    
    due_back = datetime.today()+timedelta(days=15)
    print(due_back)

    context = {
        "object": user_object,        
    }

    return render(request, "library/my-book-detail.html", context, {
        'author': book_detail.author
    })

@login_required
def pre_booking_detail(request, id):

    booking =  BookInstance.objects.get(id=id)
    # print(booking.book)

    context = {
        "booking": booking
    }

    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    profile = Profile.objects.filter(user=user).get()

    obj = get_object_or_404(BookInstance, book=booking.book)    
    due_back = datetime.today()+timedelta(days=15)
    form = BookInstanceForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():            
            obj.due_back = due_back
            obj.borrower = request.user
            obj.status = 'r'
            form.save()

            booking_status = {
                "messages": "You have renewed the book."
            }    
            messages.success(request, f'Your of {booking.book} renewed.')
            return redirect('/library/mybooks/')

        else:
            return HttpResponse('Some thing went wrong in submit. Please try again!')

    else:
        return render(request, "library/pre_booking.html", context)
    
    return render(request, "library/pre_booking.html", context)

class MyObjectReservation(ProductReservationView):
    base_model = BookInstance
    amount_field = 1
