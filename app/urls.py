from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('agencies/<int:pk>/', views.agency_detail, name='agency_detail'),
    path('about/', views.about, name='about'),
]