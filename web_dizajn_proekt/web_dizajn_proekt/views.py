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
def search(req):
    if req.user.is_authenticated:
          q=req.POST.get("search_query")
          
    return HttpResponseRedirect(reverse("getPlants",kwargs={"q":q,"page":1}))
def getPlantsList(req,q,page=1,):
    results = getPlants(API_KEY,q,page)
    context={"query_results":results,"query":str(q)}

    return render(req,"home.html",context) 

def getPlants(api_key,quer,page=1):
        print(quer)
        result = requests.get("https://perenual.com/api/species-list",params={"key": api_key,"q":quer,"page":page,})
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