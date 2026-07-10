from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('connect/', views.connect, name='connect'),
    path('about/', views.about, name='about'),
]
