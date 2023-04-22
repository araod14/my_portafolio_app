from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path("", views.game_view, name="game"),
]