from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTests(APITestCase):
    def test_register_user(self):
        url = reverse("user:create")
        data = {
            "email": "testuser@example.com",
            "password": "testpassword123",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_obtain(self):
        User.objects.create_user(
            email="testuser@example.com", password="testpassword123"
        )
        url = reverse("user:token_obtain_pair")
        data = {"email": "testuser@example.com", "password": "testpassword123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_manage_user(self):
        user = User.objects.create_user(
            email="testuser@example.com", password="testpassword123"
        )
        self.client.force_authenticate(user=user)
        url = reverse("user:manage")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "testuser@example.com")
