from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from BookStoreApp.models import Books, Users
from BookStoreApp.serializers import BooksSerializer, UsersSerializer

@csrf_exempt
def books_list(request):
    if request.method == 'GET':
        books = Books.objects.all()
        books_serializer = BooksSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    elif request.method == 'POST':
        books_Data = JSONParser().parse(request)
        books_serializer = BooksSerializer(data=books_Data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse(books_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(books_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        users_Data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_Data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def books_details(request, pk):
    try:
        books = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        books_serializer = BooksSerializer(books)
        return JsonResponse(books_serializer.data)
    elif request.method == 'PUT':
        books_data = JSONParser().parse(request)
        books_serializer = BooksSerializer(books, data = books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse(books_serializer.data)
        return JsonRespone(books_serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        books.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def users_details(request, pk):
    try:
        users = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        users_serializer = UsersSerializer(users)
        return JsonResponse(users_serializer.data)
    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(users, data = users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
