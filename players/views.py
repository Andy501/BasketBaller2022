from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (ListView,
                                 DetailView, UpdateView,DeleteView)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from players.Serializers import PlayersSerializer


from django.db.models import Q
from .models import Points, Players
from .forms import PointsUpdateForm



def landingPage(request):
    return render(request, "players/landing_page.html")

#List all players
class PlayersList(ListView):
    model = Points
    


#ad pk and routing. 
def tweets(request, pk):
    #get object tweet by pk
    #include display as tweet card inside points_detail.
    return render(request, "players/twitter_feed.html")

#detail view routed through click of player name in list view
##points updatable through form
#TODO: V3 points updatable by AJAX on players latest tweet
#points default at 0 when player created

######################HERE
# https://www.youtube.com/watch?time_continue=234&v=wXG11HcJtOw&feature=emb_title
#https://www.youtube.com/results?search_query=djagno+call+image+url
#  https://www.etutorialspoint.com/index.php/356-how-to-display-image-from-database-in-django
# i think i can do something like {static record.img}   ###in db save the image name as text. 
class PlayersDetailView(DetailView):
    model = Points

#####and template can filter through using opropriate oop. 

####If that doesnt work.....
#TODO: NOW add shoe table details to Player/points detail page using include feature and pk

#TODO: Add tweet real routing to to Player/points detail page using include feature and pk

#Update PPG and Total Points
class PlayersUpdateView(UpdateView):
    
    
    model = Points
    form_class = PointsUpdateForm
   

   #routes back to Players List. PlayersList(ListView)
    def get_success_url(self):
        return reverse('players:p_details', args=[int(self.object.player.id)])


def search(request):
    # https://linuxhint.com/build-a-basic-search-for-a-django/

    results = [] # capture and array. 

    if request.method == "GET": 
        query = request.GET.get('search')

        if query == '': #if queary is blank do this.
            query = 'None'  #passed through if statment in template

        #http://docs.djangoproject.com/en/1.1/ref/models/querysets/#icontains
        #patern DBclass.objects.filter(Q(dbclass_field_icontains=query) | Q(author_name__icontains=query) | Q(price__icontains=query) )
        # )

        #get_url method on db pointing back to "p_details"
        
        results = Players.objects.filter(Q(f_name__icontains=query) | Q(l_name__icontains=query))
    
    return render(request, 'players/search_results.html', {'query':query, 'results':results})




#TODO GET THIS APP ONLINE AWS
@api_view(['GET'])
def player_api_list(request):
    if request.method == "GET":
        players = Players.objects.all()
        serializer = PlayersSerializer(players, many=True) #True tells djano to batch many objects
        return Response(serializer.data)