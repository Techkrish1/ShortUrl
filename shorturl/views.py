# views.py

from django.shortcuts import render, HttpResponse, redirect
import random
from .models import urlModel,Userdetail
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
import random

def home(request):
    return render(request, 'landingPage.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        email=request.POST['email']
        user=Userdetail.objects.filter(email=email)
        if len(user)==0:
            ob=Userdetail()
            ob.username=request.POST['name']
            ob.email=email
            password=request.POST['password']
            ob.password=make_password(password)
            ob.save()
            return render(request,'login.html')
    return render(request,'register.html')

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

def displayUrl(request,short):
    url=urlModel.objects.filter(shorturl=short)
    if len(url)>0:
        full_url = request.build_absolute_uri('/')
        created_shorturl =full_url + url[0].shorturl
        return render(request, 'urlcreated.html', {"shorturl": created_shorturl, 'longurl': url[0].longurl})
    return render(request, 'urlcreated.html', {"shorturl": short})


@csrf_exempt 
def createurl(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            longurl=data['plainurl']
            user_ID=data['user_ID']
            if not longurl.startswith('http://') and not longurl.startswith('https://'):
                longurl = 'http://' + longurl  # Add http:// as a default prefix
            shorturl_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&^'
            shorturl = ''.join(random.sample(shorturl_letters, 6))
            if user_ID!=0:
                userid=Userdetail.objects.get(user_id=user_ID)
                
                null_rows = urlModel.objects.filter(shorturl='')
                if len(null_rows)>0:
                    null_rows[0].shorturl=shorturl
                    null_rows[0].longurl=longurl
                    null_rows[0].url_user_id=userid
                    null_rows[0].save()
                else:
                    urlModel.objects.create(longurl=longurl, shorturl=shorturl,url_user_id=userid)
            else:
                null_rows = urlModel.objects.filter(shorturl='')
                if len(null_rows)>0:
                    null_rows[0].shorturl=shorturl
                    null_rows[0].longurl=longurl
                    null_rows[0].save()
                else:
                    urlModel.objects.create(longurl=longurl, shorturl=shorturl)
            full_url = request.build_absolute_uri('/')
            created_shorturl =full_url + shorturl
            return JsonResponse({'shorturl':full_url+"created/"+shorturl})
        except Exception as e:
            print(e)
            return JsonResponse({'shorturl':""})
    return JsonResponse({'shorturl':""})


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
    
def getMyUrls(request,user_id):
    if user_id:
        myOb=urlModel.objects.filter(url_user_id=user_id)
        full_url = request.build_absolute_uri('/')
        if len(myOb)>0:
            return render(request,'myurls.html',{'myUrl':myOb,'baseurl':full_url})
    return render(request,'myurls.html')



@csrf_exempt 
def saveuser(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
            email=data['email']
            password=data['password']
            user=Userdetail.objects.filter(email=email)
            if len(user)==0:
                return JsonResponse({'user_id':0})
            isValidPassword=check_password(password,user[0].password)
            if isValidPassword:
                return JsonResponse({'user_id':int(user[0].user_id)})
        except Exception as e:
            print(e)
            return JsonResponse({'user_id':0})
    return JsonResponse({'user_id':0})



