from .models import Module, Student, Semester, SpecialisationTrack, Lecturer, GraduateProgram

"""
This file includes helper/util functions for the view layer.

get_context_for_home: Combines the process of getting all data for home view.
get_student_for_context: Checks if the logged-in user is of type STUDENT.
"""


def get_context_for_home(modules, request):
    semesters = Semester.objects.all()
    specialisation_tracks = SpecialisationTrack.objects.all()
    credits = sorted(set(Module.objects.values_list('credits', flat=True)))
    lecturers = Lecturer.objects.all()
    student = get_student_for_context(request)
    graduate_programs = GraduateProgram.objects.all()

    context = {'modules': modules,
               'module_count': modules.count(),
               'semesters': semesters,
               'specialisation_tracks': specialisation_tracks,
               'credits': credits,
               'lecturers': lecturers,
               'graduate_programs': graduate_programs
               }

    # Check if logged-in user is of type STUDENT
    if student is not None:
        context['student'] = student

    return context


def get_student_for_context(request):
    try:
        return Student.objects.get(user=request.user)
    except:
        return None
