from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','user','created']
    search_fields = ['name','user']
    list_filter = ['user']
    list_per_page = 10
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['Book_Image','name','user','author','created','filesize']
    list_filter = ['category']
    search_fields = ['name','user','author','category']
    list_per_page = 10
