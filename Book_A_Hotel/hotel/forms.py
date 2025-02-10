from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['hotel', 'room', 'customer_name', 'check_in', 'check_out']