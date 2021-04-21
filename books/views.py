from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm, RequestForm
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def details(request, id):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
    book=Book.objects.get(id=id)
    return render(request, 'details.html', {'book': book, 'form': form})

def new_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'new.html', context)