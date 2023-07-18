from django.urls import path

from .views import main, game, records

urlpatterns = [
    path('', main, name='main'),
    path('game/', game, name='game'),
    path('records/', records, name='records')
]
