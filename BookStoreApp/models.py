from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=False, null=False)

class Users(models.Model):
    firstname = models.CharField(max_length=200, blank=False, null=False)
    lastname = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    contactno = models.IntegerField(blank=True, null=False)
