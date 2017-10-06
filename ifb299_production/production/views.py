from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from production.forms import *

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            profile = profile_form.save(commit=False)

            if profile.user_id is None:
                profile.user_id = new_user.id
            profile.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'production/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def signin(request):
    return render(request, 'registration/login.html')

def error(request):
    return HttpResponse("Oops. This shouldn't be possible. You've entered a URL that's not valid.")

def home(request):
    return render(request, 'production/home.html')

def loggedout(request):
    return render(request, 'production/loggedout.html')