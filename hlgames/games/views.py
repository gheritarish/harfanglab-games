from rest_framework import viewsets

from games.serializer import GameSerializer, PlatformSerializer
from games.models import Game, Platform


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().select_related()
    serializer_class = GameSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
