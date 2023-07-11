from django.urls import path

from .views import main, game, check

urlpatterns = [
    path('', main, name='main'),
    path('game/', game, name='game'),
    path('check/', check, name='check'),
]
