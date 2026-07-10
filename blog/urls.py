from django.urls import path

from blog import views
from blog.feeds import EchoesFeed

urlpatterns = [
    path('', views.echoes, name='echoes'),
    path('archive/', views.echoes_archive, name='echoes_archive'),
    path('feed/', EchoesFeed(), name='echoes_feed'),
    path('<int:echo_id>/', views.echo_legacy_redirect, name='echo_legacy_redirect'),
    path('<slug:slug>/', views.echo_unique_page, name='echo_unique_page'),
]
