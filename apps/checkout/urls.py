from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('confirm/', views.confirm_order, name='confirm'),
    path('success/<int:order_id>/', views.order_success, name='success'),
]