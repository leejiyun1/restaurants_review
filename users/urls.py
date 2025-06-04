from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from .views import UserSignupView, UserDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    #  JWT 관련 URL
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # 일반 로그아웃도 가능하도록 남겨둡니다.
    path('session-logout/', LogoutView.as_view(), name='user-logout'),
]
