from django.urls import path, include
from rest_framework import routers
from . views import StateUpdateView, StateDestroyView, StateDetailsView

app_name = 'country'
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(r'^state/(?P<pk>\d+)$', StateDetailsView.as_view()),
    path(r'^state/(?P<pk>\d+)/update$', StateUpdateView.as_view()),
    path(r'^state/(?P<pk>\d+)/delete$', StateDestroyView.as_view())

    # path('country/state/', views.StateByCountryViewSet, name='state-list')
]