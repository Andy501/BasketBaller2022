from django.contrib import admin
from django.urls import path

from UI_Navigate.views import HomePage, Coming_Soon


#NEed load pictures fuction.

# https://basketballer-crud-demo-ardiy.ondigitalocean.app/home/


app_name = 'UI_nav'


urlpatterns = [
    path('', HomePage.as_view(), name='home'), 


    # path('coming_soon', Coming_Soon.as_view(), name='soon'),
]
