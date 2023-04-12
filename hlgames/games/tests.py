import uuid

from rest_framework.test import APITestCase

from games.models import Game, Platform


class TestPlatformListing(APITestCase):
    def test_list_platforms(self):
        Platform.objects.create(name="PC")
        Platform.objects.create(name="PS4")
        response = self.client.get("/platforms/")
        self.assertEqual(response.status_code, 200)
        data = [elt["name"] for elt in response.json()]
        data = set(data)
        self.assertEqual(data, set(["PC", "PS4"]))

    def test_put_platforms(self):
        response = self.client.post("/platforms/", {"name": "PC"}, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Platform.objects.count(), 1)


class TestGameListing(APITestCase):
    def setUp(self):
        platform = Platform.objects.create(name="PC")
        game = Game.objects.create(
            id=uuid.uuid4(),
            name="Heroes of might and magic 3",
            studio="Ubisoft",
            release_date="1999-02-14",
            ratings=20,
        )
        game.platforms.set([platform])

    def test_list_games(self):
        response = self.client.get("/games/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        data = response.json()[0]

        self.assertEqual(data["name"], "Heroes of might and magic 3")
        self.assertEqual(data["ratings"], 20)
        self.assertEqual(data["platforms"], [{"name": "PC"}])

    def test_filter_name(self):
        response = self.client.get("/games/?name=test")
        self.assertEqual(len(response.json()), 0)

        response = self.client.get("/games/?name=Heroes of might and magic 3")
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], "Heroes of might and magic 3")

    def test_filter_ratings(self):
        response = self.client.get("/games/?ratings=12")
        self.assertEqual(len(response.json()), 0)

        response = self.client.get("/games/?ratings=20")
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], "Heroes of might and magic 3")
