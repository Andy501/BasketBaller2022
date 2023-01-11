from django.shortcuts import render
from django.views import View

# Create your views here.


class Weather(View):

    def get(self, request):
        template = "FE_Weather/index.html"
        return render(request, template_name=template)
