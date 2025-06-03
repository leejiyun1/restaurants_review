from django.urls import path
from .views import UserSignupView, UserLoginView, UserDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
