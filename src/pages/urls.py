from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.homePageView, name='home'),
    url('contact/', views.contactPageView, name='contact')
]