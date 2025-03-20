
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthenticationForm

app_name = 'accounts'  

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/publisher/', views.register_publisher, name='register_publisher'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=CustomAuthenticationForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('publisher/dashboard/', views.publisher_dashboard, name='publisher_dashboard'),
    path('publisher/profile/update/', views.PublisherProfileUpdate.as_view(), name='publisher_profile_update'),
]

