from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),
    path('team/create/', views.team_create, name='team_create'),
    path('team/<int:pk>/update/', views.team_update, name='team_update'),
    path('player/create/', views.player_create, name='player_create'),
    path('player/<int:pk>/', views.player_detail, name='player_detail'),
]

#if settings.DEBUG:
#   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
