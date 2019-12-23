from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect
from blogApp.form import saveform
from blogApp.models import *
from django.contrib.auth import login
from django.contrib.auth.models import ppl
from django.urls import reverse


# Create your views here.
def index(req):
    return render(req,'index.html')



    return render(req,'login.html')
def signup(req):
    if req.method == 'POST':

        form1 = saveform(req.POST)
        print(req.POST['full_name'])
        print(req.POST['username'])
        print(req.POST['pwd'])
        print(req.POST['pwd2'])
        if req.POST['pwd'] != req.POST['pwd2']:
            return render(req,'signup.html',{'error':'password must be same'})
        else:

        
            if form1.is_valid():
                form1.save(commit=True)
                return login(req)
            else:
                return render(req,'signup.html',{'error':'enter valid data'})
            
    

    return render(req,'signup.html')
def login1(request):
    if request.method == 'POST':
        username = request.POST['text']
        password = request.POST['pass']

        user = auth.authenticate(username=username, pwd=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def home(req):
    posts = blogpost.objects.all()
    print(posts)


    return render(req,'home.html',{'blogs':posts})

