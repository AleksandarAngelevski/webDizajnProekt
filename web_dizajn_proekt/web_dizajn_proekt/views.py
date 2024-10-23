from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Favourite
from django.urls import reverse
import requests
API_KEY = "" 


def homeRedirect(req):
    return HttpResponseRedirect(reverse("home"))
def home(req,query= None,quer=""):
    if req.user.is_authenticated:
        context={}
        if query:
             context={"query_results":query,"query":quer}
        return render(req,"home.html",context)
    else:
        return HttpResponseRedirect(reverse("login"))
def search(req):
    if req.user.is_authenticated:
        q=req.POST.get("search_query")
        return HttpResponseRedirect(reverse("getPlants",kwargs={"q":q,"page":1}))  
    else:
        return HttpResponseRedirect(reverse("login"))

def getPlantsList(req,q,page=1,):
    if req.user.is_authenticated:
        results = getPlants(API_KEY,q,page)
        if results.get("error_code"):
            context={"error_api":results,}     
        else:
            context={"query_results":results,"query":str(q),"current_page":results["current_page"],"range":range(results['current_page'],results['current_page']+5),"last_page":results['last_page'],"prev_page":results['current_page']-1,}

        return render(req,"home.html",context) 
    else:
        return HttpResponseRedirect(reverse("users:login"))

def getPlants(api_key,quer,page=1):
        print(quer)
        result = requests.get("https://perenual.com/api/species-list",params={"key": api_key,"q":quer,"page":page,})
        if result.status_code == 200:
            print(result.json())
            return result.json()
        else :
            print(result.json())
            return {"error_api":"API ERROR","error_code":result.status_code}
def getPlant(req,id):
    if(req.user.is_authenticated):
        plantGuide= getPlantGuide(API_KEY,id)
        plantDetails= getPlantDetails(API_KEY,id)
        context= {"plant_guide":plantGuide,"plant_details":plantDetails,"is_favourite":False,}
        if plantGuide.get("error_code") or plantDetails.get("error_code"):
            
            context={"error_api":plantDetails}
        try:
            plant =Favourite.objects.get(plant_id=id,user_id=req.user.id)
            context["is_favourite"]= True     
            return render(req,"plant_details.html",context)
                
            
        except Favourite.DoesNotExist:
            
            return render(req,"plant_details.html",context)
        
    else:
         return HttpResponseRedirect("login")

    
      
def getPlantDetails(api_key,plant_id):
        print(id)
        result = requests.get("https://perenual.com/api/species/details/"+str(plant_id),params={"key":API_KEY,})
        if result.status_code == 200:
            
            return result.json()
        else :
            print(result.json())
            return {"error_api":"API ERROR","error_code":result.status_code}
def getPlantGuide(api_key,plant_id):
        result = requests.get("https://perenual.com/api/species-care-guide-list",params={"species_id":plant_id,"key":API_KEY})
        if result.status_code == 200:
            print(result.json()['data'][0])
            return result.json()['data'][0]
        else :
            
            return {"error_api":"API ERROR","error_code":result.status_code}
def myGarden(req):
    if req.user.is_authenticated:
        plants = Favourite.objects.filter(user_id=req.user.id)
        query_results=[]
        for plant in plants:
            query_results.append({"id":plant.plant_id,"default_image":{"regular_url":plant.img_src,},"scientific_name":plant.latin_name,"common_name":plant.plant_name})
        print(query_results)
        return render(req,"my_garden.html",{"query_results":query_results,})
    else:
        return HttpResponseRedirect(reverse("login"))

def aboutUs(req):
    if req.user.is_authenticated:
        return render(req,"about_us.html")
    else:
        return HttpResponseRedirect(reverse("login"))
    
def addFavourite(req,id):
     if req.user.is_authenticated:
        user1 = User.objects.get(pk=req.user.id)
        try:
            plant =Favourite.objects.get(plant_id=id,user=user1)
            plant.delete()

        except Favourite.DoesNotExist:
            details_temp = getPlantDetails(API_KEY,id)
            plant_temp = Favourite.objects.create(plant_id=details_temp["id"],img_src=details_temp["default_image"]["regular_url"],plant_name=details_temp["common_name"],latin_name=details_temp["scientific_name"][0],user_id=user1.id)
            plant_temp.save()


        return HttpResponseRedirect(reverse("getPlant",kwargs={"id":id}))
     else:
        return HttpResponseRedirect(reverse("login"))

    
