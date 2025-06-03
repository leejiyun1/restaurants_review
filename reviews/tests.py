from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from restaurants.models import Restaurant
from reviews.models import Review

class ReviewAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            nickname='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(email='test@example.com', password='testpass123')

        self.restaurant = Restaurant.objects.create(
            name='Test Place',
            address='123 Road',
            contact='010-1234-5678'
        )
        self.review = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            title='Good!',
            comment='Nice food'
        )

    def test_get_review_list(self):
        url = reverse('review-list', args=[self.restaurant.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_review(self):
        url = reverse('review-list', args=[self.restaurant.id])
        response = self.client.post(url, {
            'title': 'Yummy',
            'comment': 'Very nice!'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_review_detail(self):
        url = reverse('review-detail', args=[self.review.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_review(self):
        url = reverse('review-detail', args=[self.review.id])
        response = self.client.patch(url, {'title': 'Updated Title'})
        self.assertEqual(response.status_code, 200)

    def test_delete_review(self):
        url = reverse('review-detail', args=[self.review.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
