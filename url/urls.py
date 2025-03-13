from django.urls import path
from . import views

urlpatterns = [
    path('<str:hash>/', views.redirect_original_url),
    path('', views.create_short_url),
    path('stats/<str:hash>/', views.get_url_stats),
    path('all/shorts/', views.get_all_urls),
    path('all/shorts/<str:hash>/', views.get_url_by_hash),
    path('all/shorts/<str:hash>/update/', views.update_visit_count),
]