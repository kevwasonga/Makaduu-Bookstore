from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('my-books/', views.MyBooksListView.as_view(), name='my-books'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('<slug:slug>/edit/', views.BookUpdateView.as_view(), name='book-update'),
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
]