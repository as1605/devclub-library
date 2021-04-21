from django.contrib import admin
from .models import Book, Request, Issue, Return
# Register your models here.
admin.site.register(Book)
admin.site.register(Request)
admin.site.register(Issue)
admin.site.register(Return)