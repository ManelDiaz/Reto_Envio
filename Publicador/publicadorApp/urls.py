from django.urls import path
from publicadorApp import views

urlpatterns = [
    path('', views.index, name='index'),
]