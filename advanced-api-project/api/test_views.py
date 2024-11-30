# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2020)
        self.serializer = BookSerializer(instance=self.book)

    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filtering(self):
        response = self.client.get(reverse('book-list'), {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_searching(self):
        response = self.client.get(reverse('book-list'), {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering(self):
        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_permissions(self):
        # Test that only authenticated users can create, update, and delete books
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('book-list'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Test that authenticated users can create, update, and delete books
        user = self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('book-list'), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
self.client.login(username='your_username', password='your_password')
self.client.force_authenticate(user=self.user)

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('testuser', 'testuser@example.com', 'password')
        self.client.force_authenticate(user=self.user)