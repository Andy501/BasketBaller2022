from django.shortcuts import render
from django.views import View
# Create your views here.


class HomePage(View):

    def get(self, request):
        template = "business/about.html"
        return render(request, template_name=template)



