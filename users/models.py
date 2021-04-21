from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    issuedid = models.IntegerField(default=0)

class Librarian(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
