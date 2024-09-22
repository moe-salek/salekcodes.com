from django.urls import path

from blog import views

urlpatterns = [
    path('', views.echoes, name='echoes'),
    path('<int:echo_id>/', views.echo_unique_page, name='echo_unique_page'),
]
