from rest_framework import generics, viewsets

from games.serializer import GameSerializer, PlatformSerializer
from games.models import Game, Platform


class GameViewSet(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.select_related()

        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name=name)

        ratings = self.request.query_params.get("ratings")
        if ratings:
            queryset = queryset.filter(ratings=ratings)

        return queryset


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
