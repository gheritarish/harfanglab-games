from django.shortcuts import render

from rest_framework import viewsets

from games.serializer import GameSerializer
from games.models import Game


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().select_related()
    serializer_class = GameSerializer
