from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
router = DefaultRouter()
router.register('category',CategoryViewset)
router.register('books',BooksViewset)
router.register('booklist',BooksList)
urlpatterns = [
    path('',include(router.urls)),
    path('like/<int:id>/',GetLikeBooks.as_view())
]
