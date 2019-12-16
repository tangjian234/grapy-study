from django.urls import path

from . import views

urlpatterns = [
  # /tutorial
  # https://tutorial.djangogirls.org/en/django_urls/
  path('', views.home, name='home'),
  path('signin', views.sign_in, name='signin'),
  path('callback', views.callback, name='callback'),
  path('signout', views.sign_out, name='signout'),
  path('calendar', views.calendar, name='calendar'),
  path('onedrive', views.onedrive, name='onedrive'),
  path('onedrive', views.onedrive, name='onedrive'),
  #path('input', views.input, name='input'),
  path('get_mail', views.get_mail, name='get_mail'),
  
  path('profile', views.profile, name='profile'),

]