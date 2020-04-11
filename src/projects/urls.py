from django.urls import path, include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

app_name = 'projects'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]