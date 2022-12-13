from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
router = DefaultRouter()
router.register('category',CategoryViewset)
router.register('books',BooksViewset)
urlpatterns = [
    path('',include(router.urls))
]
