from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import requests
API_KEY = "sk-XYRt66e73d2fc02095961"

def home(req,query= None,quer=""):
    if req.user.is_authenticated:
        context={}
        if query:
             context={"query_results":query,"query":quer}
        return render(req,"home.html",context)
    else:
        return HttpResponseRedirect("login")

def getPlantsList(req,page_number=1):
     if req.user.is_authenticated:
          q=req.POST.get("search_query")
          results = getPlants(req,API_KEY,q,page_number)
          context={"query_results":results,"query":q}
          return render(req,"home.html",context)

def getPlants(req,api_key,quer,page_number=1):
        print(quer)
        result = requests.get("https://perenual.com/api/species-list",params={"key": api_key,"q":quer,})
        if result.status_code == 200:
            print(result.json())
            result=result.json()
            return result
        else :
            print(result.json())
            return {"error":"API ERROR"}.json()
def getPlant(req,id):
     pass
def getPlantDetails(api_key,query):
        result = requests.get("https://perenual.com/api/species-list",params={"key": API_KEY,"q":query,})
        if result.status_code == 200:
            print(result.json())
            result=result.json()
            return result
        else :
            print(result.json())
            return {"error":"API ERROR"}.json()
def getPlantGuide(api_key,plant_id):
        result = requests.get("https://perenual.com/api/species/details",params={"key": API_KEY,"ID":plant_id,})
        if result.status_code == 200:
            print(result.json())
            result=result.json()
            return result
        else :
            print(result.json())
            return {"error":"API ERROR"}.json()
def myGarden(req):
     pass
def aboutUs(req):
    if req.user.is_authenticated:
        return render(req,"about_us.html")
    else:
        return HttpResponseRedirect("login")