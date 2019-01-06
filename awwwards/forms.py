from .models import *
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']
        