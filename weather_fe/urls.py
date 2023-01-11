from django.contrib import admin
from django.urls import path

from weather_fe.views import Weather



app_name = 'Weathered'


# BASE URL NEEDS WEATHER ADDED. 

#JS and staic needs associations. 


urlpatterns = [
    path('weather/', Weather.as_view(), name='wea_fe'),
]
