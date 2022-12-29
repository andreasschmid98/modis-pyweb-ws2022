from django.db import models
from django.db.models import Q

from .graduate_program import GraduateProgram
from .lecturer import Lecturer
from .semester import Semester
from .specialisation_track import SpecialisationTrack


class Module(models.Model):
    """
    This class represents a Module and is the core class of modis.
    It is also responsible for filtering and sorting of the Module instances.
    For more information on the advantages of this, see
    https://spookylukey.github.io/django-views-the-right-way/thin-views.html#example-push-filtering-to-the-model-layer
    """

    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    learning_objective = models.TextField(null=True, blank=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True)
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
    def sort_modules_by_title(modules, direction):
        if direction == 'desc':
            return modules.order_by('-title')
        return modules.order_by('title')

    @staticmethod
    def filter_modules_by_search_query(search_query):
        return Module.objects.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(learning_objective__icontains=search_query) |
            Q(lecturer__last_name__icontains=search_query) |
            Q(lecturer__first_name__icontains=search_query)
        ).distinct()

    @staticmethod
    def filter_modules_by_semester(search_query):
        semester = Semester.objects.filter(type=search_query)
        return Module.objects.filter(semesters__in=semester)

    @staticmethod
    def filter_modules_by_graduate_program(search_query):
        # split search_query into title and degree
        title, degree = search_query.replace('(', '').replace(')', '').rsplit(' ', 1)
        graduate_program = GraduateProgram.objects.filter(title=title, degree=degree)
        return Module.objects.filter(graduate_programs__in=graduate_program)

    @staticmethod
    def filter_modules_by_specialisation_track(search_query):
        specialisation_track = SpecialisationTrack.objects.filter(title=search_query)
        return Module.objects.filter(specialisation_tracks__in=specialisation_track)

    @staticmethod
    def filter_modules_by_credits(search_query):
        return Module.objects.filter(credits=search_query)

    @staticmethod
    def filter_modules_by_lecturer(search_query):
        first_name, last_name = search_query.split(' ')
        lecturer = Lecturer.objects.filter(first_name=first_name, last_name=last_name)
        return Module.objects.filter(lecturer__in=lecturer)
