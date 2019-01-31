from django import forms
from .models import SimpleGuest

class SimpleGuestForm(forms.ModelForm):

    class Meta:
        model = SimpleGuest
        fields = ('simple_guest_name',)
