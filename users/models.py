from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        if not nickname:
            raise ValueError('닉네임은 필수입니다.')

        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nickname, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    nickname = models.CharField(max_length=20, unique=True)
    profile_image = models.ImageField(
        upload_to='users/profile_images',
        default='users/blank_profile_image.png'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email
