from django.db import models
from django.contrib.auth.models import User

class Cilt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kullanıcı")
    birth_place = models.CharField(max_length=200, blank=True, null=True, verbose_name="Birth Place")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Birth date")

    def __str__(self):
        return f"{self.user.username}"
