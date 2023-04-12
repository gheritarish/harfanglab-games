from rest_framework import serializers

from games.models import Game, Platform


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = "name"


class GameSerializer(serializers.HyperlinkedModelSerializer):
    platforms = serializers.ReadOnlyField(source="platforms.name")
    class Meta:
        model = Game
        fields = ("name", "studio", "release_date", "ratings", "platforms")
