from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
#    return HttpResponse("Hello, world. You've hit the 'production' 'app' in django.")


def index(request):
    return render(request, 'production/SignIn.html')

















