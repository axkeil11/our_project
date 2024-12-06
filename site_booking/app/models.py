from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator
from phonenumber_field.modelfields import  PhoneNumberField


class User(AbstractUser):
    age=models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                         validators=[MinValueValidator(16), MaxValueValidator(100)])
    phone_number = PhoneNumberField()
    STATUS_CHOICES=(
        ('client', 'client'),
        ('owner', 'owner'),
    )
    status=models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
          return f'{self.first_name}, {self.last_name}, {self.status}'


class Country (models.Model):
    country_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.country_name


class Room(models.Model):
    NUMBER_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7')
    )
    number_status = models.CharField(max_length=10 , choices=NUMBER_CHOICES, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('available', 'available'),
        ('booked', 'booked')
    )
    room_status = models.CharField(max_length=32, choices=STATUS_CHOICES, null=True, blank=True)
    price = models.PositiveSmallIntegerField(verbose_name='цена', null=True, blank=True)

    def __str__(self):
        return self.room_status


class RoomPhotos(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='room')
    room_image = models.ImageField(upload_to='room_image')



class Hotel(models.Model):
        hotel_name = models.CharField(max_length=32, unique=True)
        image = models.ImageField(upload_to='hotel_image')
        room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
        country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
        description = models.TextField(null=True, blank=True)

        def __str__(self):
            return self.hotel_name

        def get_average_rating(self):
            ratings = self.reviews.all()
            if ratings.exists():
                return round(sum(i.stars for i in ratings)/ ratings.count(), 1)
            return 0



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    stars =models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}'

