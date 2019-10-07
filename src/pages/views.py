from django.http import HttpResponse
from django.urls import reverse
# from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.template import loader

# Create your views here.


def home_view(request, *args, **kwargs):
    appName = 'smartUniv'
    print(request.user)
    return render(request, "home.html", {'appName': appName})


# def contact_view(request, *args, **kwargs):
#     return render(request, "contact.html", {})
    # return HttpResponse("<h2>I am contact page </h2>")


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def appname(request):
    return {'appname': reverse(request.path).app_name}


