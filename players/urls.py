from django.urls import path
from .views import PlayersList, PlayersDetailView, PlayersUpdateView, player_api_list
from players import views


app_name="players"

urlpatterns = [
    path('', views.landingPage, name='home'), 
    path('search/search/', views.search, name='search'), 
    path('heat/', PlayersList.as_view(), name='p_list'), 
    path('heat/<pk>/',PlayersDetailView.as_view(), name="p_details"), 
    path('heat/update/<pk>/',PlayersUpdateView.as_view(), name="p_update"), 
    path('api/heat/',views.player_api_list), 
]
