# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.urls import reverse


#Create your models here.
class HotelModel(models.Model):
    hotelName = models.CharField(max_length=255)
    Price = models.FloatField()
    hotel_image = models.ImageField(upload_to='images/', max_length=2083)
    Hotel_options = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=100, choices=Hotel_options, default='active')
    hotelPlace = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return '{}'.format(self.hotelName)

    def get_absolute_url(self):
        return reverse('api:hotel', args=[self.slug])

    @property
    def image_url(self):
        if self.hotel_image:
            return self.hotel_image.url
        return '#'


class RoomAvailable(models.Model):
    hotel = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    roomNumber = models.CharField(max_length=255, null=False)
    Room_options = (
        ('empty', 'Empty'),
        ('Occupied', 'Occupied'),
    )
    Room_availability = models.CharField(max_length=100, choices=Room_options, default='empty')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return '{}'.format(self.roomNumber)

    def get_absolute_url(self):
        return reverse('api:RoomAvailable', args=[self.slug])


class GuestReservation(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name='Customer Name')
    mobileNumber = models.IntegerField(null=False, blank=False, verbose_name='Mobile No', unique=True)
    Age = models.IntegerField()
    hotel = models.CharField(max_length=255, verbose_name='Hotel Name')
    room_number = models.CharField(max_length=255, null=False)

