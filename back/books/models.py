from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from datetime import datetime
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name=_("Category Name"),help_text=_("Enter category name"))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    @property
    def date(self):
        mydate = self.created
        return mydate.strftime("%m/%d/%Y, %H:%M:%S")
    @property
    def bookscount(self):
        kitoblar = len(self.books.all())
        return kitoblar

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=_("Categories ")
        db_table = "Categories"
class Book(models.Model):
    name = models.CharField(max_length=200,verbose_name=_("Book Name"),help_text=_("Enter book name"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,verbose_name=_("Choose Category(ies)"), help_text=_("Choose categoy(ies)"),related_name='books')
    image = models.ImageField(upload_to='book-images',verbose_name=_("Book Image"), help_text=_("Upload book image"))
    author = models.CharField(max_length=150,verbose_name=_("Book Author"), help_text=_("Enter book author"))
    about = models.TextField(verbose_name=_("Book Description"), help_text=_("Upload book description"))
    file = models.FileField(upload_to='book-files',verbose_name=_("Book File"), help_text=_("Upload book file"))
    book_pages = models.CharField(max_length=150, verbose_name=_("Book Pages"), help_text=_("Enter book pages"))
    viewed = models.IntegerField(default=1)
    downloaded = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    @property
    def bookcomments(self):
        return list(self.comments.all().values())
    @property
    def commentscount(self):
        return len(self.comments.all())
    @property
    def Book_Image(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%"'.format(self.image.url))
    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=_("Books ")
        db_table = "Books"
class Comments(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    description = models.TextField(verbose_name=_('Comment'),help_text=_("Enter comment"))
    added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description
    class Meta:
        db_table = 'Comments'
        verbose_name = _('Comments')
        verbose_name_plural = _('Comments')
    


