from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/loggedin')
    else:
        form = UserCreationForm()
    return render(request, 'production/signup.html', {'form': form})

def signin(request):
    return render(request, 'registration/login.html')

def index(request):
    return HttpResponse("Oops. This shouldn't be possible. You've entered a URL that's not valid.")

def loggedin(request):
    return render(request, 'production/home.html')

def loggedout(request):
    return render(request, 'production/loggedout.html')