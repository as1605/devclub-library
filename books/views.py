from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})