from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# get the custom user model
User = get_user_model()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class GraduateProgram(models.Model):
    class Degree(models.TextChoices):
        BACHELOR = 'B', _('Bachelor')
        MASTER = 'M', _('Master')

    title = models.CharField(max_length=200)
    degree = models.CharField(max_length=2, choices=Degree.choices)

    def __str__(self):
        return f'{self.title} ({self.degree})'


class SpecialisationTrack(models.Model):
    title = models.CharField(max_length=200)
    graduate_program = models.ForeignKey(GraduateProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Semester(models.Model):
    class Type(models.TextChoices):
        WINTER = 'WS', _('Winter-Semester')
        SUMMER = 'SS', _('Sommer-Semester')

    type = models.CharField(max_length=2, choices=Type.choices)

    def __str__(self):
        return self.type


class Module(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    learning_objective = models.TextField(null=True, blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True)
    semesters = models.ManyToManyField(Semester)
    graduate_programs = models.ManyToManyField(GraduateProgram)
    specialisation_tracks = models.ManyToManyField(SpecialisationTrack)

    credits = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @staticmethod
    def filter_modules_by_search_query(search_query):
        return Module.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(learning_objective__icontains=search_query) |
            Q(lecturer__last_name__icontains=search_query) |
            Q(lecturer__first_name__icontains=search_query) |
            Q(semesters__type__icontains=search_query) |
            Q(graduate_programs__title__icontains=search_query) |
            Q(specialisation_tracks__title__icontains=search_query) |
            Q(credits=(int(search_query) if search_query.isdigit() else False))
        ).distinct()
