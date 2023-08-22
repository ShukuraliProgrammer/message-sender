from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    birth_day = models.DateTimeField(null=True, blank=True)
    telegram_id = models.CharField(verbose_name="User's telegram Id", max_length=60, unique=True)

    def __str__(self):
        return self.telegram_id

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Message(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Message that have to send")

    def __str__(self):
        return self.text
