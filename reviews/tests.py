from django.test import TestCase
from django.contrib.auth import get_user_model
from restaurants.models import Restaurant
from reviews.models import Review

User = get_user_model()

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="reviewer@example.com",
            nickname="reviewer",
            password="password"
        )
        self.restaurant = Restaurant.objects.create(
            name="이탈리안 레스토랑",
            address="서울시 송파구",
            contact="02-999-8888"
        )
        self.review = Review.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            title="맛있어요",
            comment="정말 훌륭한 음식이었습니다."
        )

    def test_create_review(self):
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(self.review.title, "맛있어요")
