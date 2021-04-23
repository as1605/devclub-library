from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from books.models import Book, Request, Issue, Return
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.groups.add(2)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Student account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if (request.user.is_staff):
        return redirect("admin:index")
    obj = []
    req = Request.objects.filter(userid=request.user.id)
    req = req[::-1]
    for r in req:
        b = Book.objects.get(id=r.bookid)
        if Issue.objects.filter(requestid=r.id).count()>0:
            i = Issue.objects.get(requestid=r.id)
        else:
            i = None
        if i is not None and Return.objects.filter(issueid=i.id).count()>0:
            ret = Return.objects.get(issueid=i.id)
        else:
            ret = None
        obj.append({
            "req": r,
            "book": b,
            "iss": i,
            "ret": ret,
        })
    return render(request, 'users/profile.html', {'obj': obj})