from django.urls import path, include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'courses'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('/$', views.course_list)
]

