from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_list,name='book-list'),
    path('new/',views.book_form,name='book-new'),
    path('<int:id>',views.book_detail),
    path('requests/',views.request_list,name='request-list'),
    path('requests/<int:id>',views.request_detail),
    path('issued/',views.issue_list,name='issue-list'),
    path('issued/<int:id>',views.issue_detail),
    path('returns/',views.return_list,name='return-list'),
]