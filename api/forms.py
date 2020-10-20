from django import forms
from .models import *


class GuestForm(forms.ModelForm):
    class Meta:
        model = GuestReservation
        fields = '__all__'