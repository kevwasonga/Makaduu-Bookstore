from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='detail'),
    path('add/<int:book_id>/', views.cart_add, name='add'),
    path('remove/<int:book_id>/', views.cart_remove, name='remove'),
]