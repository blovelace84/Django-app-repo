
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def hello(request):
    return HttpResponse("<h1>Hello</h1> <p>World</p>")
urlpatterns = [
    path('admin-site/', admin.site.urls),
    path('hello', hello)
]
