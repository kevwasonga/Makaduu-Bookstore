from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Subscriber, ContactMessage
from .forms import ContactForm, SubscriberForm
from apps.books.models import Book

def home(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('core:home')
    else:
        form = SubscriberForm()
    
    featured_books = Book.objects.filter(status=Book.PUBLISHED).order_by('-created_at')[:4]
    
    context = {
        'subscriber_form': form,
        'featured_books': featured_books,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})
