from django.urls import path 
from .import views

urlpatterns = [
path("Welcome/", views.Welcome, name='Welcome'),
path("Show/",views.Show, name='show'),
]