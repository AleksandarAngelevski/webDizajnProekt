from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginF
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
            return render(req,"home.html")
        return render(req,"login.html")