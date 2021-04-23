from django import forms

from .models import Book, Request, Issue, Return

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
        ]

class IssueForm(forms.ModelForm):
    class Meta:
        model=Issue
        fields = [
            'due',
        ]

class ReturnForm(forms.ModelForm):
    class Meta:
        model=Return
        fields = [
        ]