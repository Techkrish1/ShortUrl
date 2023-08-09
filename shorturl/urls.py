from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('go', views.makeshorturl),
    path("<str:shorturl>", views.redirecturl)
]
