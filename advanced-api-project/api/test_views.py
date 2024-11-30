from django.test import TestCase
from api.models import Book
from django.contrib.auth.models import User
from rest_framework import status

class ApiTestCase(TestCase):
    def setup(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': '2001',
        }

    def test_create_book(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post('/api/books/create/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
        self.assertEqual(response.data['author'], self.book_data['author'])
        self.assertEqual(response.data['publication_year'], self.book_data['publication_year'])



    def test_create_book_unauthorized(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post('/api/books/create/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



    def test_update_book(self):
        Book.objects.create(**self.book_data)
        response = self.client.get('/api/books/')
        self.assertequal(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # def test_get_book()