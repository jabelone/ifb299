from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signin/$', auth_views.login, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/$', views.search, name='search'),
    url(r'^signout/$', auth_views.logout, {'next_page': '/loggedout'}, name='logout'),
    url(r'^loggedout/$', views.loggedout, name='loggedout'),
    url(r'^data-admin/$', views.data_admin, name='data_admin'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^howto/$', views.howto, name='howto'),
    url(r'^whatif/$', views.whatif, name='whatif'),
    url(r'^cani/$', views.cani, name='cani'),
    url(r'^$', views.home, name='home'),
]