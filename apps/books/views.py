from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from apps.core.mixins import PublisherRequiredMixin

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        return Book.objects.filter(status=Book.PUBLISHED).order_by('-created_at')

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(status=Book.PUBLISHED)

class MyBooksListView(LoginRequiredMixin, PublisherRequiredMixin, ListView):
    model = Book
    template_name = 'books/my_books.html'
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        return Book.objects.filter(publisher=self.request.user).order_by('-created_at')

class BookCreateView(LoginRequiredMixin, PublisherRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:my-books')

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        messages.success(self.request, 'Book created successfully!')
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, PublisherRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:my-books')

    def get_queryset(self):
        return Book.objects.filter(publisher=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)
