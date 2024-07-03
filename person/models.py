from django.db import models

from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_place = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.birth_place} - {self.birth_date}"