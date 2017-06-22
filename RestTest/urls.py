from django.conf.urls import url, include
from rest_framework import routers
from restclient import views
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='RestClient API')

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'universities', views.UniversityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/',schema_view),
    url(r'^', include('restclient.urls')),
]