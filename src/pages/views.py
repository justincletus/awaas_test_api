from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World.</h1>")
    # template = loader.get_template('template/home.html')
    print(request.user)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
    # return HttpResponse("<h2>I am contact page </h2>")


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


