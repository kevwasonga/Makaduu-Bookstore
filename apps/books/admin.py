from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'price', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'publication_date']
    search_fields = ['title', 'description', 'isbn']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publication_date'
    ordering = ['-created_at']
