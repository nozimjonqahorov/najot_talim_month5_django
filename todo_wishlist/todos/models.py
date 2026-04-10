from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    STATUS_CHOICES = [
        ("hali bajarilmagan", "Hali bajarilmagan"),
        ("bajarilmoqda", "Bajarilmoqda"),
        ("bajarilgan", "Bajarilgan")
    ]
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=450)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=400, choices= STATUS_CHOICES)

    class Meta:
        verbose_name = 'Vazifa'
        verbose_name_plural = 'Vazifalar'

    def __str__(self):
        return f"{self.user} | {self.title} | {self.deadline}"
    