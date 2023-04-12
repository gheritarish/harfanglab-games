from django.db import models


class Platform(models.Model):
    name = models.TextField(primary_key=True, max_length=20)


class Game(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(max_length=200, null=False)
    studio = models.TextField(max_length=100, null=False)
    release_date = models.DateField(null=False)
    ratings = models.IntegerField(null=True)
    platforms = models.ForeignKey(Platform, on_delete=models.CASCADE)
