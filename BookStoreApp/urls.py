from django.conf.urls import url
from BookStoreApp import views

urlpatterns = [
    url(r'^apis/v1/books', views.books_list),
    url(r'^apis/v1/users', views.users_list),
    url(r'^apis/v1/book/(?P<pk>[0-9]+)$', views.books_details),
    url(r'^apis/v1/user/(?P<pk>[0-9]+)$', views.users_details),
]
