from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('saveuser/',views.saveuser,name='saveuser'),
    path('createurl/',views.createurl,name='createurl'),
     path('myurl/<user_id>/',views.getMyUrls,name='myurls'),
    path('shortener', views.makeshorturl),
    path('created/<short>/',views.displayUrl,name='displayurl'),
    path("<str:shorturl>", views.redirecturl)
]
