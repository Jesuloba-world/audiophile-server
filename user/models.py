from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address", unique=True
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
