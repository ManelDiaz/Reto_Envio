from django.urls import path
from subscriptorApp import views

urlpatterns = [
    path('', views.ListaMensajesView.as_view(), name='index'),
]