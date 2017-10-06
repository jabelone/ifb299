from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from production.models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type',)# 'phone', 'address')