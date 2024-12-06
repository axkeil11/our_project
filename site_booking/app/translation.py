from .models import Hotel, Room, Country
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)