from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from .models import Book, Request, Issue, Return
from .forms import BookForm, RequestForm, IssueForm, ReturnForm
# Create your views here.


@permission_required('books.view_book')
def index(request):
    books = Book.objects.all()
    q=request.GET.get("q")
    title=request.GET.get("title")
    author=request.GET.get("author")
    publisher=request.GET.get("publisher")
    genre=request.GET.get("genre")
    summary=request.GET.get("summary")
    ISBN=request.GET.get("ISBN")
    available=request.GET.get("available") 
    t = []
    if q:
        for b in books:
            if available and not b.available:
                continue
            if title and b.title.upper().find(title.upper())>=0:
                t.append(b)
            elif author and b.author.upper().find(author.upper())>=0:
                t.append(b)
            elif publisher and b.publisher.upper().find(publisher.upper())>=0:
                t.append(b)
            elif genre and b.genre.upper().find(genre.upper())>=0:
                t.append(b)
            elif summary and b.summary.upper().find(summary.upper())>=0:
                t.append(b)
            elif ISBN and b.ISBN.upper().find(ISBN.upper())>=0:
                t.append(b)
        books = t
    return render(request, 'books/book_list.html', {'books': books})


@permission_required('books.add_book')
def new_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Book successfuly saved!")
        body = "Hi "+str(request.user.username)+"! "
        body +="You have added a new book "
        body +=str(form.instance.title)
        body +=" by "
        body +=str(form.instance.author)
        body +=". Book ID: "
        body +=str(form.instance.id)
        body +=". Thanks for using our library!"
        send_mail("Book added", body, "devclub.library@gmail.com", {request.user.email},fail_silently=True)
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
        form.instance.userid = request.user.id
        form.save()
        messages.success(request, "Book successfuly requested!")
        body = "Hi "+str(request.user.username)+"! "
        body +="You have requested a book "
        body +=str(object.title)
        body +=" by "
        body +=str(object.author)
        body +=". Book ID: "
        body +=str(object.id)
        body +=". Thanks for using our library!"
        send_mail("Book requested", body, "devclub.library@gmail.com", {request.user.email},fail_silently=True)
    return render(request, 'books/book_detail.html', {'object': object, 'form': form})


@permission_required('books.view_request')
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
        body = "Hi "+str(obj["student"].username)+"! "
        body +="Your book request has been approved! You have been issued "
        body +=str(obj["book"].title)
        body +=" by "
        body +=str(obj["book"].author)
        body +=". Book ID: "
        body +=str(obj["book"].id)
        body +=". Please return it by "
        body +=str(form.instance.due)
        body +=". Thanks for using our library!"
        send_mail("Book issued", body, "devclub.library@gmail.com", {obj["student"].email},fail_silently=True)
    return render(request, 'books/request_detail.html', {'obj': obj, 'form': form})


@permission_required('books.view_issue')
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
        body = "Hi "+str(obj["student"].username)+"! "
        body +="You have returned "
        body +=str(obj["book"].title)
        body +=" by "
        body +=str(obj["book"].author)
        body +=". Book ID: "
        body +=str(obj["book"].id)
        body +=". Thanks for using our library!"
        send_mail("Book returned", body, "devclub.library@gmail.com", {obj["student"].email},fail_silently=True)
    return render(request, 'books/issue_detail.html', {'obj': obj, 'form': form})


@permission_required('books.view_return')
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
