from django.contrib import admin

from .models import Student, Lecturer, Module, GraduateProgram, Semester, SpecialisationTrack

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Module)
admin.site.register(GraduateProgram)
admin.site.register(Semester)
admin.site.register(SpecialisationTrack)
