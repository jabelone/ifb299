from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You've hit the 'production' 'app' in django. ~yolo")
