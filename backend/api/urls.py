from django.urls import path
from . import views

urlpatterns = [
    path('services/m', views.hello, name='hello'),  # Maps the URL to the view
]