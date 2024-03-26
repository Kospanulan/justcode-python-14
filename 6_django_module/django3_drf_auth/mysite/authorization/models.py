from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from authorization.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    SUPERUSER, MODERATOR, APPUSER = 1, 2, 3

    ROLES = (
        (SUPERUSER, 'Superuser'),
        (MODERATOR, 'Moderator'),
        (APPUSER, 'AppUser')
    )

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    role = models.IntegerField(default=APPUSER, choices=ROLES)

    date_joined = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



