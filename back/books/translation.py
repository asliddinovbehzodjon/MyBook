from .models import Category,Book
from modeltranslation.translator import TranslationOptions,register
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ['name']
@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields=['name','about','file']