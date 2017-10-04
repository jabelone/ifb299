from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', views.signIn, name='signIn'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^$', views.index, name='index'),
]
