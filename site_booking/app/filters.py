from django_filters import FilterSet
from .models import Hotel


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['exact'],
            'country': ['exact'],
            'room': ['exact']
        }


