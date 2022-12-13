from rest_framework import serializers
from .models import Category,Book
class CategorySerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    bookcount = serializers.SerializerMethodField('books_soni')

    def books_soni(self, obj):
        return obj.bookscount
    class Meta:
        model = Category
        fields = ['name','books','bookcount','created','updated','user','name_en','name_ru']
class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model =Book
        fields = "__all__"