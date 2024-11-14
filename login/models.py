from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Qo'shimcha maydonlar kerak bo'lsa bu yerga qo'shishingiz mumkin
    pass

class UserProfile(models.Model):
    pass
