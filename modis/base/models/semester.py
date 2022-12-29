from django.db import models


class Semester(models.Model):
    class Type(models.TextChoices):
        WINTER = 'Wintersemester'
        SUMMER = 'Sommersemester'

    class Meta:
        ordering = ['type']

    type = models.CharField(max_length=20, choices=Type.choices)

    def __str__(self):
        return self.type
