from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre= models.CharField(max_length=255)
    summary = models.TextField()
    ISBN = models.CharField(max_length=13)
    location = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
    img = models.URLField(max_length=2083)

class Request(models.Model):
    userid= models.IntegerField()
    bookid= models.IntegerField()
    requesttime = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField()

class Issue(models.Model):
    userid= models.IntegerField()
    requestid = models.IntegerField()
    approvetime= models.DateTimeField(auto_now_add=True)
    due= models.DateTimeField()

class Return(models.Model):
    userid= models.IntegerField()
    issueid = models.IntegerField() 
    returntime= models.DateTimeField(auto_now_add=True)