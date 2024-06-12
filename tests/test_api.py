from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from api.models import Actor


class TheatreTests(APITestCase):
    def test_create_actor(self):
        url = reverse('actor-list-create')
        data = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_actors(self):
        Actor.objects.create(first_name='John', last_name='Doe')
        url = reverse('actor-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
