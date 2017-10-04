from django.http import HttpResponse
from django.shortcuts import render


def registration(request):
    return render(request, 'production/Registration.html')

def signIn(request):
    return render(request, 'production/SignIn.html')

def index(request):
    return HttpResponse("Oops. This shouldn't be possible. You've entered a URL that's not valid.")
