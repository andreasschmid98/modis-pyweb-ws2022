from django.db import models

from .graduate_program import GraduateProgram


class SpecialisationTrack(models.Model):
    title = models.CharField(max_length=200)
    graduate_program = models.ForeignKey(GraduateProgram, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
