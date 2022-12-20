from django_filters import rest_framework as filters

from books.models import Book


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields ={
            'name':['icontains'],
            'author':['icontains'],
            'about':['icontains']
        }