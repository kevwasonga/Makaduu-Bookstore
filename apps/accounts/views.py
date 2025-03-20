from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import UserRegistrationForm, PublisherRegistrationForm, PublisherProfileForm
from .models import User
from apps.books.models import Book

@login_required
def publisher_dashboard(request):
    if not request.user.is_publisher:
        messages.error(request, 'You must be a publisher to access this page.')
        return redirect('core:home')
    
    published_books = Book.objects.filter(publisher=request.user)
    
    context = {
        'published_books': published_books,
    }
    
    return render(request, 'accounts/publisher_dashboard.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('core:home')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Makaduu Bookstore.')
            return redirect('core:home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def register_publisher(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please register as a user first before applying for publisher status.')
        return redirect('accounts:register')
        
    if request.user.is_publisher:
        messages.info(request, 'You are already registered as a publisher.')
        return redirect('accounts:publisher_dashboard')
    
    if request.method == 'POST':
        form = PublisherRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                'Your publisher account request has been submitted. An admin will review it shortly.'
            )
            return redirect('accounts:publisher_dashboard')
    else:
        form = PublisherRegistrationForm(instance=request.user)
    
    return render(request, 'accounts/register_publisher.html', {'form': form})

class PublisherProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = PublisherProfileForm
    template_name = 'accounts/publisher_profile.html'
    success_url = reverse_lazy('accounts:publisher_dashboard')

    def test_func(self):
        return self.request.user.is_publisher

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)
