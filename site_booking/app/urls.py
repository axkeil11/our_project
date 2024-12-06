from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user',UserViewSet, basename='user')
router.register(r'room', RoomViewSet,basename='room')
router.register(r'review',ReviewViewSet, basename='review')
router.register(r'country',CountryViewSet, basename='country')


urlpatterns = [
    path('',include(router.urls)),
    path('hotel/',HotelListApiView.as_view(), name='hotel_list' ),
    path('hotel/<int:pk>/', HotelDetailApiView.as_view(), name='hotel_detail')

]