from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from production.models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', ) #'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type',)# 'phone', 'address')