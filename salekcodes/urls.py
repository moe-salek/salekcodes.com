from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),
    # path('api/blog/', include('blog.urls')),  # TODO
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
