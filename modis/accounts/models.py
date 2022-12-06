from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    LECTURER = 1
    STUDENT = 2
    ADMIN = 3

    USER_TYPE_CHOICES = (
        (LECTURER, 'LECTURER'),
        (STUDENT, 'STUDENT'),
        (ADMIN, 'ADMIN'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


