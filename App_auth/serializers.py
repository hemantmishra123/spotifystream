from rest_framework import serializers
from django.contrib.auth.models import User
from.models import Song 

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

