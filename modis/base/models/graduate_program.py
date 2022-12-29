from django.db import models


class GraduateProgram(models.Model):
    class Degree(models.TextChoices):
        BACHELOR = 'Bachelor'
        MASTER = 'Master'

    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=200)
    degree = models.CharField(max_length=20, choices=Degree.choices)

    def __str__(self):
        return f'{self.title} ({self.degree})'
