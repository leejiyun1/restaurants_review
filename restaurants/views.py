from rest_framework.viewsets import ModelViewSet
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = []  # 추후 인증 기능 추가 시 설정 예정
