"""
URL configuration for web_dizajn_proekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views
from . import views

urlpatterns = [
    path("",views.homeRedirect,name="homeRedirect"),
    path('admin/', admin.site.urls),
    path('users/',include("users.urls")),
    path("home/",views.home,name="home"),
    path("home/plants/list/<str:q>/<int:page>/",views.getPlantsList,name="getPlants"),
    path("home/plants/<int:id>",views.getPlant,name="getPlant"),
    path("home/plants/myGarden/",views.myGarden,name="myGarden"),
    path("about/",views.aboutUs,name="aboutUs"),
    path("search/",views.search,name="search"),
    path("favourite/<int:id>",views.addFavourite,name="favourite")
]
