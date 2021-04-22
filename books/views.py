from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import permission_required

from .models import Book
from .forms import BookForm, RequestForm
# Create your views here.

#def index(request):
#    books = Book.objects.all()
#    return render(request, 'books/index.html', {'books': books})

#@permission_required('books.view_book')
class BookListView(ListView):
    model=Book
    template_name='books/index.html'
    context_object_name='books'
    ordering = ['title']
    paginate_by = 20


@permission_required('books.add_request')
def details(request, id):
#    if request.user.groups.filter(id=2).count()==0 and not request.user.is_superuser:
#        return HttpResponse("Only students can view or request books")
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Book successfuly requested!")
    object=Book.objects.get(id=id)
    return render(request, 'books/book_detail.html', {'object': object, 'form': form})

@permission_required('books.add_book')
def new_book(request):
#    if request.user.groups.filter(id=1).count()==0 and not request.user.is_superuser:
#        return HttpResponse("Only librarians can create new books")
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'books/book_form.html', context)