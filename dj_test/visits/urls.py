from django.urls import path

from . import views

ap_name = 'visits'

url_patterns = [
    path('', views.index, name='index')
]