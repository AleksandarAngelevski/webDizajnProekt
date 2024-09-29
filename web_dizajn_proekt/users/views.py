from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginF
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
# Create your views here.
def login(req):
    user= None
    if req.user.is_authenticated:
        return render(req,"home.html")
    else:
        if req.method=="POST":
            print("!")
            user = authenticate(username=req.POST.get("username"),password=req.POST.get("password"))
        if user is not None:
            loginF(req,user)
            return HttpResponseRedirect("home")
        return render(req,"login.html",{"error":"Invalid username/password"})
def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            print()
            if form.errors["username"] and form.errors["password2"]:
                return render(req,"register.html",{"form":UserCreationForm,"errors":{"username":"Username already exists","password":"Password too weak"}})    
            elif form.errors["username"]:
                return render(req,"register.html",{"form":UserCreationForm,"errors":{"username":"Username already exists",}})    
            elif form.errord["password"]:
                return render(req,"register.html",{"form":UserCreationForm,"errors":{"password":"Password too weak"}})    
            return render(req,"register.html",{"form":UserCreationForm,"error":form.errors})
    return render(req, "register.html",{"form":UserCreationForm})

def logOut(req):
    pass