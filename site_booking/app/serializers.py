from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_status', ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class HotelListSerializer(serializers.ModelSerializer):
    country = CountrySerializer( read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id','hotel_name', 'image', 'country', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()



class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'image', 'description', 'country', 'room']
