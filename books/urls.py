from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('new',views.new_book),
    path('<int:id>',views.details),
]