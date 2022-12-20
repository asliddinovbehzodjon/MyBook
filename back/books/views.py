from django.shortcuts import render
#################
from rest_framework.response import Response
from rest_framework.decorators import action
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

from .filter import BookFilter
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
# Create your views here.
from .models import Category,Book
from .serializer import CategorySerializer,BookSerializer
from rest_framework.viewsets import ModelViewSet
class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class BooksViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    @action(detail=True, methods=['get','post'])
    def addview(self, request,pk):
         book = Book.objects.get(id=pk)
         book.viewed = book.viewed+1
         book.save()
         return Response({'status':'Added view'})

    @action(detail=True, methods=['get', 'post'])
    def adddownloaded(self, request, pk):
        book = Book.objects.get(id=pk)
        book.downloaded = book.downloaded + 1
        book.save()
        return Response({'status': 'Downloaded'})