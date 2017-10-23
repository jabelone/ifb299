from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from production.forms import *
from production.models import Data
from django.db.models import Q

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
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
        user_form = SignUpForm()
        profile_form = ProfileForm()

    return render(request, 'production/signup.html', {'user_form': user_form, 'profile_form': profile_form})

def search(request):
    if request.method == 'POST':
        data = None
        print("posting")
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            print("form valid")
            data_type = search_form.cleaned_data.get('data_type')
            print(data_type)
            if (data_type == "College"):
                data = Data.objects.all().filter(Q(data_type="School") | Q(data_type="College"))
            elif (data_type):
                data = Data.objects.all().filter(data_type=data_type)

    else:
        search_form = SearchForm()
        data = "first_request"

    return render(request, 'production/search.html', {'search_form': search_form, 'data': data})

def signin(request):
    return render(request, 'registration/login.html')

def error(request):
    return HttpResponse("Oops. This shouldn't be possible. You've entered a URL that's not valid.")

def home(request):
    return render(request, 'production/home.html')

def loggedout(request):
    return render(request, 'production/loggedout.html')

def contacts(request):
    return render(request, 'production/contacts.html')

def howto(request):
    return render(request, 'production/howto.html')

def whatif(request):
    return render(request, 'production/whatif.html')

def cani(request):
    return render(request, 'production/cani.html')

def data_admin(request):
    if request.method == 'POST':
        admin_form = AdminForm(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            admin_form = AdminForm()
            return render(request, 'production/admins.html', {'submitted': True, 'admin_form': admin_form})

    else:
        admin_form = AdminForm()

    return render(request, 'production/admins.html', {'admin_form': admin_form})
