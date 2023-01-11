"""niacom2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from NiacomLanding.views import HomePage


app_name = 'portfolio'

######TODO: START DOCKER FOR DEV of project FIRST
#####TODO make the overall landing page for Portifolio
#######TODO connect relavant settings and routing to this location to basketballer. 
urlpatterns = [
    path('home/', HomePage.as_view(), name='home'), 
]
