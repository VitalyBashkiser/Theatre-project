from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Actor


class TheatreTests(APITestCase):
    def setUp(self):
        self.url = '/api/theatre/actors/'

    def test_create_actor(self):
        data = {"first_name": "John", "last_name": "Doe"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_actors(self):
        Actor.objects.create(first_name="John", last_name="Doe")
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["first_name"], "John")
        self.assertEqual(response.data[0]["last_name"], "Doe")
