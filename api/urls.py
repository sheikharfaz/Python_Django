from django.urls import path
from . import views,apiviews

app_name = 'api'

urlpatterns = [
    path('guest-list/', views.guest_list, name='guest_list'),
    path('guest-create/', views.guest_create, name='guest_create'),
    path('guest-edit/<int:pk>', views.guest_edit, name="guest_edit"),
    path('guest-delete/<int:pk>', views.guest_delete, name="guest_delete"),
        path('hotel-search/', views.hotel_header, name="hotel_search"),
]