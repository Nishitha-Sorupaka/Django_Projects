from rest_framework import serializers
from testapp.models import *
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movies','year','genre','rating','one_line','stars','votes','runtime','gross']
