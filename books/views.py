from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from .models import Book, Request, Issue, Return
from .forms import BookForm, RequestForm, IssueForm, ReturnForm
# Create your views here.

#def index(request):
#    books = Book.objects.all()
#    return render(request, 'books/index.html', {'books': books})

#@permission_required('books.view_book')
class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    ordering = ['title']
    paginate_by = 20


@permission_required('books.add_book')
def new_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Book successfuly saved!")
    context = {
        'form': form
    }
    return render(request, 'books/book_form.html', context)


@permission_required('books.add_request')
def details(request, id):
    form = RequestForm(request.POST or None)
    object = Book.objects.get(id=id)
    if form.is_valid():
        form.instance.bookid = object.id
        form.instance.userid = id
        form.save()
        messages.success(request, "Book successfuly requested!")
    return render(request, 'books/book_detail.html', {'object': object, 'form': form})


@permission_required('books.add_issue') #should have been a more relevant permission
def requests(request):
    reqs = Request.objects.all()
    reqs = reqs[::-1]
    obj = []
    for r in reqs:
        u = User.objects.get(id=r.userid)
        b = Book.objects.get(id=r.bookid)
        obj.append({
            "req": r,
            "student": u,
            "book": b,
        })
    return render(request, 'books/request_list.html', {'obj': obj})


@permission_required('books.add_issue')
def approve(request, id):
    r = Request.objects.get(id=id)
    u = User.objects.get(id=r.userid)
    b = Book.objects.get(id=r.bookid)
    obj = {
        "req": r,
        "student": u,
        "book": b,
    }
    form = IssueForm(request.POST or None)
    if form.is_valid():
        form.instance.requestid=obj["req"].id
        form.save()
        obj["book"].available=False
        obj["book"].save()
        obj["req"].approved=True
        obj["req"].save()
        messages.success(request, "Book successfully issued!")
    return render(request, 'books/request_detail.html', {'obj': obj, 'form': form})


@permission_required('books.add_return') #should have been a more relevant permission
def issued(request):
    issues = Issue.objects.all()
    issues = issues[::-1]
    obj = []
    for i in issues:
        r = Request.objects.get(id=i.requestid)
        u = User.objects.get(id=r.userid)
        b = Book.objects.get(id=r.bookid)
        obj.append({
            "iss": i,
            "req": r,
            "student": u,
            "book": b,
        })
    return render(request, 'books/issue_list.html', {'obj': obj})


@permission_required('books.add_return')
def returned(request, id):
    i = Issue.objects.get(id=id)
    r = Request.objects.get(id=i.requestid)
    u = User.objects.get(id=r.userid)
    b = Book.objects.get(id=r.bookid)
    obj = {
        "iss": i,
        "req": r,
        "student": u,
        "book": b,
    }
    form = ReturnForm(request.POST or None)
    if form.is_valid():
        form.instance.issueid=obj["iss"].id
        form.save()
        obj["book"].available=True
        obj["book"].save()
        obj["iss"].returned=True
        obj["iss"].save()
        messages.success(request, "Book successfully returned!")
    return render(request, 'books/issue_detail.html', {'obj': obj, 'form': form})


@permission_required('books.add_return') #should have been a more relevant permission
def returns(request):
    rets = Return.objects.all()
    rets = rets[::-1]
    obj = []
    for ret in rets:
        i = Issue.objects.get(id=ret.issueid)
        r = Request.objects.get(id=i.requestid)
        u = User.objects.get(id=r.userid)
        b = Book.objects.get(id=r.bookid)
        obj.append({
            "ret": ret,
            "iss": i,
            "req": r,
            "student": u,
            "book": b,
        })
    return render(request, 'books/return_list.html', {'obj': obj})
