from django.urls import path
from . import views

urlpatterns = [
    path('poop/', views.hello),
    path('about/', views.about),
]