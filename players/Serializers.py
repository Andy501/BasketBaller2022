from rest_framework import serializers
from .models import Players


class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Players
        fields = ['f_name', 'l_name', 'number']