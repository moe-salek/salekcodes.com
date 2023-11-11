from django.urls import path

from blog.views import PostView

urlpatterns = [
    path('posts/<int:id>/', PostView.as_view(), name='post_retrieve'),
    path('posts/', PostView.as_view(), name='post_list'),
]
