from django.shortcuts import render, HttpResponse, redirect
import random
from .models import urlModel


def home(request):
    return render(request, 'landingPage.html')

# Creating a short url for the original long url

def makeshorturl(request):
    if request.method == 'POST':
        longurl = request.POST['longurl']
        shorturl_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&^'
        shorturl = (''.join(random.sample(shorturl_letters,6)))
        obj = urlModel.objects.create(longurl= longurl, shorturl= shorturl)  #  It is creating and saving an object in a single step
        created_shorturl = "http://127.0.0.1:8000/" + shorturl
    return render(request, 'urlcreated.html', {"shorturl":created_shorturl, 'longurl': longurl})

# When redirecting using the short url

def redirecturl(request, shorturl):
    try:
        obj = urlModel.objects.get(shorturl = shorturl)
    except urlModel.DoesNotExist:
        obj = None

    if obj != None:
        obj.count+=1
        obj.save()
        return redirect(obj.longurl)
    else:
        return render(request, 'url_error.html')

