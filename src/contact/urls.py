from django.urls import path, include
from rest_framework import routers
from contact import views

app_name = 'contact'
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('^contact/$', 'contact_collection'),
    # path('^contact/<?P<pk>[^/]+/$', 'contact_element')
]