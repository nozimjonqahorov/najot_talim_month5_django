from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="users/", blank=True, null=True, default="users/default_user.jpg")
    age = models.PositiveIntegerField(blank=True, null=True)



    class Meta:
        db_table = "CustomUser"
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"


    def __str__(self):
        return f"{self.username} | ({self.email})"
    