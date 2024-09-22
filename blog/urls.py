from django.urls import path

from blog import views

urlpatterns = [
    path('', views.echoes, name='echoes'),
    path('archive/', views.echoes_archive, name='echoes_archive'),
    path('<int:echo_id>/', views.echo_unique_page, name='echo_unique_page'),
]
