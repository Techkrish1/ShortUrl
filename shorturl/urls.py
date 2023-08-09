from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('shortener', views.makeshorturl),
    path("<str:shorturl>", views.redirecturl)
]
