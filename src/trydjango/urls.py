"""
smart university all url lists.
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import re_path, url
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from django.contrib.auth import views as auth_views
from djreservation import urls as djreservation_urls
from rest_framework import routers
from contact import views as contact_views
from content import views as content_views
# from api import views as api_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt import views as jwt_views


from pages.views import (
    home_view,
    about_view
)

router = routers.DefaultRouter()
# router.register(r'contact', contact_views.contact_collection)
router.register(r'contact', contact_views.ContactViewSet)
router.register(r'content', content_views.ContentViewSet)
# router.register(r'api', api_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='homepage'),
    path('about/', about_view, name='about'),
    path('signup/', core_views.signup, name='signup'),
    path('accounts/profile/', core_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('products/', include('products.urls', namespace="products")),
    path('library/', include('library.urls', namespace="library")),
    path('core/', include('core.urls')),
    re_path(r'^', include(router.urls)),
    re_path(r'^contact/', include('contact.urls')),
    re_path(r'^content/', include('content.urls')),
    re_path(r'^api/', include('api.urls')),
    # re_path(r'^posts/', include('microblog.urls')),
    re_path(r'', include('microblog.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + djreservation_urls.urlpatterns




# urlpatterns += + djreservation_urls.urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

