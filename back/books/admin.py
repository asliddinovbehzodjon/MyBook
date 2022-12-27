from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import *
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name','user','date','bookscount']
    fields = ['name']
    search_fields = ['name','user']
    list_filter = ['user']
    list_per_page = 10
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
@admin.register(Book)
class BookAdmin(TranslationAdmin):
    list_display = ['Book_Image','name','user','author','created','filesize','viewed','downloaded','commentscount']
    list_filter = ['category']
    search_fields = ['name','user','author','category']
    list_per_page = 10
    fields = ['name','category','image','author','about','file','book_pages']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['description','book']
    search_fields = ['description']
admin.site.register(Comments,CommentsAdmin)