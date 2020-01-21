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
from country import views as country_views
from country import custom_url
from university import views as university_views
from colleges import views as college_views
# from api import views as api_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt import views as jwt_views
from courses import views as course_view
from category import views as cat_views

from pages.views import (
    home_view,
    about_view
)

router = routers.DefaultRouter()
# router.register(r'contact', contact_views.contact_collection)
router.register(r'contact', contact_views.ContactViewSet)
router.register(r'content', content_views.ContentViewSet)

new_router = custom_url.CustomReadOnlyRouter()
# new_router.register(r'country/state/', country_views.StateByCountryViewSet)

router.register(r'country', country_views.CountryViewSet)
router.register(r'states', country_views.StateViewSet)

# router.register(r'country/state/', country_views.StateByCountryViewSet)
# router.register(r'state_country', country_views.StateByCountry, 'State')
router.register(r'city', country_views.CityViewSet)
router.register(r'urban', country_views.UrbanViewSet)
router.register(r'university', university_views.UniversityViewSet)
router.register(r'colleges', college_views.CollegeViewSet)
router.register(r'category', cat_views.CategoryViewSet)

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
    re_path(r'^country/', include('country.urls')),
    # path('country/state/', include('country.urls')),
    # re_path(r'^country/state/', include('country.urls')),
    # re_path(r'^city/', include('country.urls')),
    # path('urban/', include('country.urls')),
    re_path(r'^api/', include('api.urls')),
    # re_path(r'^university/', include('university.urls')),
    # re_path(r'^college/', include('colleges.urls')),
    # re_path(r'^posts/', include('microblog.urls')),
    re_path(r'', include('microblog.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    re_path(r'^courses/$', course_view.course_list),
    re_path(r'^course/(?P<pk>[0-9]+)$', course_view.course_detail),
    re_path(r'^course/(?P<slug>[-\w]+)$', course_view.course_detail_slug),
    re_path(r'^state_list/(?P<slug>[-\w]+)/$', country_views.StateByCountry),
    re_path(r'^university_list/(?P<slug>[-\w]+)$', university_views.StateByUniversity),
    re_path(r'^colleges_list/(?P<slug>[-\w]+)$', college_views.CollegesByUniversity),
    re_path(r'^state_list_country_id/(?P<pk>[0-9]+)$', country_views.StateByCountryId),
    re_path(r'^city_list/(?P<pk>[0-9]+)$', country_views.CityByState),
    re_path(r'^urban_list/(?P<pk>[0-9]+)$', country_views.UrbanByState)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + djreservation_urls.urlpatterns

# urlpatterns += + djreservation_urls.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
