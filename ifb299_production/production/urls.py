from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signin/$', auth_views.login, name='signin'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/loggedout'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^loggedout/$', views.loggedout, name='loggedout'),
    url(r'^$', views.index, name='index'),
]