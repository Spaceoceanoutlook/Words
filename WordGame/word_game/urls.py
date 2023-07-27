from django.urls import path

from .views import main, game, savedgames, delete_game

urlpatterns = [
    path('', main, name='main'),
    path('game/', game, name='game'),
    path('savedgames/', savedgames, name='savedgames'),
    path('delete_game/<int:pk>/', delete_game, name='delete_game'),
]
