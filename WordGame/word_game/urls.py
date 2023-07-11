from django.urls import path

from .views import main, game

urlpatterns = [
    path('', main, name='main'),
    path('game/', game, name='game'),
]
