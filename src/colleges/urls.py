from django.urls import path, include
from rest_framework import routers

app_name = 'colleges'
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]
