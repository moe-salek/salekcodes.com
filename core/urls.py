from django.urls import path

from core import views

urlpatterns = [
    path('', views.coming_soon, name='index'),  # TODO: change to index later
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
