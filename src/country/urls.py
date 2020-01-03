from django.urls import path, include
from rest_framework import routers

app_name = 'country'
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]