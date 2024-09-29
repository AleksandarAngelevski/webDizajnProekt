from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
API_KEY = "sk-XYRt66e73d2fc02095961"

def home(req):
    if req.user.is_authenticated:
        return render(req,"home.html")
    else:
        return HttpResponseRedirect("login")
     
def getPlants(api_key,query):
        result = requests.get("https://perenual.com/api/species-list",params={"key": API_KEY,"q":query,})
        if result.status_code == 200:
            print(result.json())
            result=result.json()
            return result
        else :
            print(result.json())
            return {"error":"API ERROR"}.json()

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