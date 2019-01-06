from .models import *
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['usability','content','design','vote_submissions']
