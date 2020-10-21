# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.urls import reverse


#Create your models here.
class HotelModel(models.Model):
    hotelName = models.CharField(max_length=255)
    Price = models.FloatField()
    Hotel_options = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=100, choices=Hotel_options, default='active')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return '{}'.format(self.hotelName)

    def get_absolute_url(self):
        return reverse('api:hotel', args=[self.slug])


class RoomAvailable(models.Model):
    hotel = models.ForeignKey(HotelModel, on_delete=models.CASCADE)
    roomNumber = models.CharField(max_length=255, null=False)
    Room_options = (
        ('empty', 'Empty'),
        ('Occupied', 'Occupied'),
    )
    Room_availability = models.CharField(max_length=100, choices=Room_options, default='empty')


class GuestReservation(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name='Customer Name')
    mobileNumber = models.IntegerField(null=False, blank=False, verbose_name='Mobile No', unique=True)
    Age = models.IntegerField()
    hotel = models.CharField(max_length=255, verbose_name='Hotel Name')
    room_number = models.ForeignKey(RoomAvailable, on_delete=models.PROTECT, default=1)

