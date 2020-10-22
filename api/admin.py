from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(HotelModel)
class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('hotelName',), }
    list_display = ['hotelName', 'Price', 'status', 'slug']


@admin.register(GuestReservation)
class GuestAdmin(admin.ModelAdmin):
        list_display = ['customer_name', 'mobileNumber', 'Age', 'hotel', 'room_number']


@admin.register(RoomAvailable)
class RoomAdmin(admin.ModelAdmin):
        list_display = [ 'hotel', 'roomNumber', 'Room_availability']


