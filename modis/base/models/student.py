from django.contrib.auth import get_user_model
from django.db import models
from .module import Module

# get the custom user model
User = get_user_model()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    favourites = models.ManyToManyField(Module, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
