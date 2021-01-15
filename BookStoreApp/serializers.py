from rest_framework import serializers
from BookStoreApp.models import Books, Users

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'name', 'author', 'user')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'firstname', 'lastname', 'email', 'contactno')
