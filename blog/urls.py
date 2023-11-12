from django.urls import path

from blog.views import PostView, TagView

urlpatterns = [
    # post:
    path('posts/<int:id>/', PostView.as_view({'get': 'retrieve'}), name='post_detail'),
    path('posts/', PostView.as_view({'get': 'list'}), name='post_list'),
    # tag:
    path('tags/<int:id>/', TagView.as_view({'get': 'retrieve'}), name='tag_detail'),
    path('tags/', TagView.as_view({'get': 'list'}), name='tag_list'),
]
