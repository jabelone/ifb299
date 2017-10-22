from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.forms import ModelForm
from production.models import *


class SignUpForm(UserCreationForm):
    user_types = forms.ChoiceField(choices=((None, ''), ('student', 'STUDENT'), ('tourist', 'TOURIST'), ('business', 'BUSINESS')))
=======
from production.models import *

class SignUpForm(UserCreationForm):
>>>>>>> master
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', )

<<<<<<< HEAD
class AdminsForm(UserCreationForm):
    user_types = forms.ChoiceField(choices=((None, ''), ('student', 'STUDENT'), ('tourist', 'TOURIST'), ('business', 'BUSINESS')))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'user_types')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'address')

=======
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'phone', 'address')
>>>>>>> master
