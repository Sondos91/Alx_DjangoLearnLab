from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        
        
class AuthorSerializer(serializers.ModelSerializer):
        books = BookSerializer(many=True, read_only=True)

  class Meta:
        model = Author
        fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'
