from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('resume/', views.resume, name='resume'),
    path('api/new-game/', views.new_game, name='new_game'),
    path('api/validate-move/', views.validate_move_api, name='validate_move'),
    path('api/load-game/', views.load_game, name='load_game'),
    path('api/get-hint/', views.get_hint_api, name='get_hint'),
    path('learn/', views.learn, name='learn'),
]