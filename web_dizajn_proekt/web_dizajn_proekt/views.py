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
    context={"query_results":results,"query":str(q),"current_page":results["current_page"],"range":range(results['current_page'],results['current_page']+5),"last_page":results['last_page'],"prev_page":results['current_page']-1,}

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
    
    plantGuide= getPlantGuide(API_KEY,id)
    plantDetails= getPlantDetails(API_KEY,id)
    return render(req,"plant_details.html",{"plant_guide":plantGuide,"plant_details":plantDetails})


    
      
def getPlantDetails(api_key,plant_id):
        print(id)
        result = requests.get("https://perenual.com/api/species/details/"+str(plant_id),params={"key":API_KEY,})
        if result.status_code == 200:
            result=result.json()
            return result
        else :
            print(result.json())
            return {"error":"API ERROR"}.json()
def getPlantGuide(api_key,plant_id):
        result = requests.get("https://perenual.com/api/species-care-guide-list",params={"species_id":plant_id,"key":API_KEY})
        if result.status_code == 200:
            print(result.json()['data'][0])
            return result.json()['data'][0]
        else :
            
            return {"error":"API ERROR"}.json()
def myGarden(req):
     pass
def aboutUs(req):
    if req.user.is_authenticated:
        return render(req,"about_us.html")
    else:
        return HttpResponseRedirect("login")