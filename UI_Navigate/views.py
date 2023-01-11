from django.shortcuts import render
from django.views import View
# Create your views here.


class HomePage(View):

    def get(self, request):
        template = "FE_Nav/index.html"
        return render(request, template_name=template)



class Coming_Soon(View):

    def get(self, request):
        template = "FE_Nav/coming_soon.html"
        return render(request, template_name=template)
