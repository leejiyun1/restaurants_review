from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from restaurants.models import Restaurant

class RestaurantViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            nickname='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(email='test@example.com', password='testpass123')
        self.restaurant = Restaurant.objects.create(
            name='Test Food',
            address='Somewhere',
            contact='010-1234-5678'
        )

    def test_restaurant_list_view(self):
        url = reverse('restaurant-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_post_view(self):
        url = reverse('restaurant-list')
        response = self.client.post(url, {
            'name': 'New Food',
            'address': 'New Address',
            'contact': '010-0000-0000'
        })
        self.assertEqual(response.status_code, 201)

    def test_restaurant_detail_view(self):
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_update_view(self):
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        response = self.client.patch(url, {'name': 'Updated Name'})
        self.assertEqual(response.status_code, 200)

    def test_restaurant_delete_view(self):
        url = reverse('restaurant-detail', args=[self.restaurant.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
