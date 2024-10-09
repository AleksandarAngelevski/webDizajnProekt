from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginF
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout_user
from django.urls import reverse
# Create your views here.
def login(req):
    user= None
    if req.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    else:
        if req.method=="POST":
            print("!")
            user = authenticate(username=req.POST.get("username"),password=req.POST.get("password"))
            if user is not None:
                loginF(req,user)
                return HttpResponseRedirect(reverse("home"))
            return render(req,"login.html",{"error":"Invalid username/password"})
    return render(req,"login.html")
    
def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            
            if form.errors.get("username") and form.errors.get("password2"):
                return render(req,"register.html",{"form":UserCreationForm,"errors":{"username":"Username already exists","password":"Password too weak"}})    
            elif form.errors.get("username"):
                return render(req,"register.html",{"form":UserCreationForm,"errors":{"username":"Username already exists",}})    
            elif form.errors.get("password2"):
                return render(req,"register.html",{"form":UserCreationForm,"errors":{"password":"Password too weak"}})    
            return render(req,"register.html",{"form":UserCreationForm,"error":form.errors})
    return render(req, "register.html",{"form":UserCreationForm})

def logOut(req):
    logout_user(req)
    return HttpResponseRedirect(reverse("login"))