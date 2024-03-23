from django.contrib import admin
from django.urls import path

urlpatterns = [
    # core:
    # path('', include('core.urls')),
    # blog:
    # path('api/blog/', include('blog.urls')),
    # admin panel:
    path('admin/', admin.site.urls)
]
