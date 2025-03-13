from django.urls import path
from . import views

urlpatterns = [
    path('<str:hash>/', views.redirect_original_url),
    path('', views.create_short_url),
    path('stats/<str:hash>/', views.get_url_stats),
]