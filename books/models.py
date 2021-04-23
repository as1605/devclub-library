from django.db import models
from django.utils import timezone
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
    img = models.URLField(max_length=2083, default="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Book_icon_%28closed%29_-_Blue_and_gold.svg/343px-Book_icon_%28closed%29_-_Blue_and_gold.svg.png")

class Request(models.Model):
    userid= models.IntegerField()
    bookid= models.IntegerField()
    requesttime = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

class Issue(models.Model):
    requestid = models.IntegerField()
    approvetime= models.DateTimeField(default=timezone.now)
    due= models.DateTimeField()
    returned = models.BooleanField(default=False)

class Return(models.Model):
    issueid = models.IntegerField() 
    returntime= models.DateTimeField(default=timezone.now)