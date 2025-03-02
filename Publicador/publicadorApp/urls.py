from django.urls import path
from publicadorApp import views

urlpatterns = [
    path('', views.MensajeCreateView.as_view(), name='index'),
]