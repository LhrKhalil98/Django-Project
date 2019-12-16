from django import forms 
from .  import models 

class CreateBooking(forms.ModelForm): 
    class Meta : 
        model= models.Booking 
        fields=['date_in','date_out', 'person' ] 