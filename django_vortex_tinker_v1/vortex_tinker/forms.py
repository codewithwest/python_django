from django import forms

class DemoForm(forms.Form):
    name = forms.CharField()

from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
