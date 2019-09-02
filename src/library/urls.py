from django.urls import path
from django.conf.urls import url

from library.views import (
    book_list_view,
    book_detail_view,
    author_list_view,
    author_detail_view,
    book_search_view,
    user_account_detail,
    pre_booking_detail,
    # MyObjectReservation,


)

app_name = 'library'

urlpatterns = [
    path('', book_list_view, name='booklist'),
    path('search/', book_search_view, name='book-search'),
    path('<int:id>/', book_detail_view, name="book-detail"),
    path('authors/', author_list_view, name="authors"),
    path('author/<int:id>/', author_detail_view, name="author-detail"),
    path('mybooks/', user_account_detail, name="user-books"),
    path('prebooking/<uuid:id>/', pre_booking_detail, name="pre-booking"),

]

# urlpatterns += [
#     url(r"^reservationroom/create/(?<pk>\d+)$", MyObjectReservation.as_view())
# ]
