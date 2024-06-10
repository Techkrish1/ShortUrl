# views.py

from django.shortcuts import render, HttpResponse, redirect
import random
from .models import urlModel

def home(request):
    return render(request, 'landingPage.html')

def makeshorturl(request):
    if request.method == 'POST':
        longurl = request.POST['longurl']
        
        # Check if the input URL starts with http:// or https://
        if not longurl.startswith('http://') and not longurl.startswith('https://'):
            longurl = 'http://' + longurl  # Add http:// as a default prefix
        
        # Rest of your existing code to create the short URL
        shorturl_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&^'
        shorturl = ''.join(random.sample(shorturl_letters, 6))
        obj = urlModel.objects.create(longurl=longurl, shorturl=shorturl)
        created_shorturl = "http://127.0.0.1:8000/" + shorturl
    return render(request, 'urlcreated.html', {"shorturl": created_shorturl, 'longurl': longurl})

def redirecturl(request, shorturl):
    try:
        obj = urlModel.objects.get(shorturl=shorturl)
    except urlModel.DoesNotExist:
        obj = None

    if obj:
        obj.count += 1
        obj.save()
        # Check if the long URL is a relative URL
        if not obj.longurl.startswith('http://') and not obj.longurl.startswith('https://'):
            obj.longurl = 'http://' + obj.longurl  # Add http:// as a default prefix
        return redirect(obj.longurl)
    else:
        return render(request, 'url_error.html')


