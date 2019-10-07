from django.urls import path, include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from content import views

# from .views import (
#     # content_list_view,
#     content_create_view,
#     # content_update_view
# )

app_name = 'content'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('', content_list_view, name="content-list"),
    # path('create/', content_create_view, name="content-create"),
    # path('<int:id>/update/', csrf_exempt(content_update_view), name="content-update"),
]