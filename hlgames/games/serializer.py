from rest_framework import serializers

from games.models import Game, Platform


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ["name"]


class GameSerializer(serializers.HyperlinkedModelSerializer):
    platforms = PlatformSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = ("id", "name", "studio", "release_date", "ratings", "platforms")
