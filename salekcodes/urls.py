from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # core:
    # path('', include('core.urls')),
    # blog:
    path('api/blog/', include('blog.urls')),
    # resume_cv:
    path('api/resume/', include('resume_cv.urls')),
    # admin panel:
    path('admin/', admin.site.urls),
    # drf:
    path('api-auth/', include('rest_framework.urls')),
    # schema:
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
