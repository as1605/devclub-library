from django import forms

from .models import Book, Request, Issue

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'publisher',
            'genre',
            'summary',
            'ISBN',
            'location',
            'available',
            'img',
        ]

class RequestForm(forms.ModelForm):
    class Meta:
        model=Request
        fields = [
            'userid',
            'bookid',
        ]
