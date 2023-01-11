


from django import forms
from .models import Points
from django.forms import ModelForm


class PointsUpdateForm(ModelForm):

    #customized form field name
    tot_points = forms.CharField(label='Season Total Points')
  
    class Meta:
        model = Points
        fields = ['tot_points','ppg']
        