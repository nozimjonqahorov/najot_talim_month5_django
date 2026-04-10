from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)

    class Meta:
        db_table = "CustomUser"
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"


    def __str__(self):
        return f"{self.username} | ({self.email})"
    