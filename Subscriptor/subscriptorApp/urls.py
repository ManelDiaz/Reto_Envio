from django.urls import path
from subscriptorApp import views

urlpatterns = [
    path('', views.index, name='index'),
]