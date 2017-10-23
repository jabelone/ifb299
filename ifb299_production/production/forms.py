from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from production.models import Profile, Data

USER_TYPES = (
    ('TOURIST', 'Tourist'),
    ('BUSINESS', 'Business'),
    ('STUDENT', 'Student'),
)

DATA_TYPES = (
    ('SCHOOL', 'School'),
    ('Business', 'Business'),
    ('TRANSPORT', 'Transport'),
)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', )

class AdminsForm(UserCreationForm):
    data_type = forms.ChoiceField(choices=DATA_TYPES, required=True )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'data_type')

class ProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=USER_TYPES, required=True)
    class Meta:
        model = Profile
        fields = ('phone', 'address', 'user_type')

class SearchForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=USER_TYPES, required=True)
    class Meta:
        model = Data
        fields = ('user_type',)