from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user',UserViewSet, basename='user')
router.register(r'room', RoomViewSet,basename='room')
router.register(r'country',CountryViewSet, basename='country')
router.register('booking', BookingViewSet, basename='booking')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('',include(router.urls)),
    path('hotel/',HotelListApiView.as_view(), name='hotel_list' ),
    path('hotel/<int:pk>/', HotelDetailApiView.as_view(), name='hotel_detail'),
    path('review', ReviewApiView.as_view(), name='review')

]