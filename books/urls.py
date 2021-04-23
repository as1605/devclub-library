from django.urls import path
from .views import BookListView
from . import views

urlpatterns = [
    path('',BookListView.as_view(),name='book-list'),
    path('new',views.new_book,name='book-new'),
    path('<int:id>',views.details),
    path('requests',views.requests,name='request-list'),
    path('requests/<int:id>',views.approve),
    path('issued',views.issued,name='issue-list'),
    path('issued/<int:id>',views.returned),
    path('returns',views.returns,name='return-list'),
]