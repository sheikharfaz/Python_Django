from rest_framework import serializers
from .models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAvailable
        fields = '__all__'
