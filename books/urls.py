from django.urls import path
from .views import BookListView
from . import views

urlpatterns = [
    path('',BookListView.as_view(),name='book-list'),
    path('new',views.new_book),
    path('<int:id>',views.details),
]