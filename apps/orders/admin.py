from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'status', 'total_amount']
    list_filter = ['status', 'created']
    search_fields = ['id', 'user__email']
    inlines = [OrderItemInline]
