from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from production.models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'phone', 'address')

class SearchForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('title', 'data_type')