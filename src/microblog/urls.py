from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', views.BlogPostViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('', include(router.urls)),
]