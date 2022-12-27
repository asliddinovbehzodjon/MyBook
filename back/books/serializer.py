from rest_framework import serializers
from .models import Category,Book,Comments
class CategorySerializer(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    bookcount = serializers.SerializerMethodField('books_soni')

    def books_soni(self, obj):
        return obj.bookscount

    class Meta:
        model = Category
        fields = ['id','name','books','bookcount','created','updated','user','name_en','name_ru']
        depth=2
class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    size = serializers.SerializerMethodField('book_size')
    comments = serializers.SerializerMethodField('mycomments')
    class Meta:
        model =Book
        fields = ['id','name','user','image','author','category','created','about','file','downloaded','viewed','book_pages','size','comments']


    def mycomments(self,obj):
        return obj.bookcomments
    def book_size(self, obj):
        return obj.filesize
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        