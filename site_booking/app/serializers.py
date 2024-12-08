from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status',)
        extra_kwargs = {'passwords':{'write only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user':{
                'username':instance.username,
                'email':instance.email,
            },
            'access':str(refresh.access_token),
            'refresh':str(refresh),
        }


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


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'user', 'start_date', 'end_date', 'is_canceled']

    def validate(self, data):
        room = data['room']
        if not room.is_available:
            raise serializers.ValidationError("Room is not available")
        if Booking.objects.filter(
                room=room,
                start_date__lt=data['end_date'],
                end_date__gt=data['start_date']
        ).exists():
            raise serializers.ValidationError("Room is already booked for the selected dates")
        return data