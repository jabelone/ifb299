from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from production.models import Profile, Data

USER_TYPES = (
    ('Tourist', 'Tourist'),
    ('Business', 'Business'),
    ('Student', 'Student'),
)

DATA_TYPES = (
    ('Select Category', 'Select Category'),
    ('College', 'College'),
    ('Library', 'Library'),
    ('Industry', 'Industry'),
    ('Hotel', 'Hotel'),
    ('Park', 'Park'),
    ('Zoo', 'Zoo'),
    ('Museum', 'Museum'),
    ('Restaurant', 'Restaurant'),
    ('Mall', 'Mall')
)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', )

class AdminForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"

class ProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=USER_TYPES, required=True)
    class Meta:
        model = Profile
        fields = ('phone', 'address', 'user_type')

class SearchForm(forms.ModelForm):
    data_type = forms.ChoiceField(choices=DATA_TYPES, required=True, widget=forms.Select(attrs={'onchange': 'submit();'}))
    class Meta:
        model = Data
        fields = ('data_type',)