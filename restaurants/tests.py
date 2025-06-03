from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from restaurants.models import Restaurant

class RestaurantViewTestCase(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="테스트 식당",
            address="서울시 중구",
            contact="02-000-0000"
        )

    def test_restaurant_list_view(self):
        url = reverse('restaurant-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_post_view(self):
        url = reverse('restaurant-list')
        data = {
            "name": "새로운 식당",
            "address": "서울시 강서구",
            "contact": "02-1234-5678"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Restaurant.objects.count(), 2)

    def test_restaurant_detail_view(self):
        url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_restaurant_update_view(self):
        url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.pk})
        data = {
            "name": "수정된 식당 이름",
            "address": self.restaurant.address,
            "contact": self.restaurant.contact
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.name, "수정된 식당 이름")

    def test_restaurant_delete_view(self):
        url = reverse('restaurant-detail', kwargs={'pk': self.restaurant.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Restaurant.objects.count(), 0)
