from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Module, Student, Semester, SpecialisationTrack, Lecturer, GraduateProgram
from .forms import ModuleForm

modules = Module.objects.all()


@login_required
def home(request):
    global modules
    search_query = request.GET.get('q') if request.GET.get('q') is not None else ''
    modules = Module.filter_modules_by_search_query(search_query)
    context = get_context_for_home(request)
    return render(request, 'home.html', context)


@login_required
def module(request, primary_key):
    module = Module.objects.get(id=primary_key)

    context = {'module': module}

    student = get_student_for_context(request)

    if student is not None:
        context['student'] = student

    return render(request, 'module.html', context)


@login_required
def create_module(request):
    form = ModuleForm(user=request.user)

    if request.method == 'POST':
        form = ModuleForm(request.POST, user=request.user)
        if form.is_valid():
            form.save(user=request.user, commit=False)
            form.save_m2m()
            return redirect('home')

    context = {'form': form}
    return render(request, 'module_form.html', context)


@login_required
def update_module(request, primary_key):
    module = Module.objects.get(id=primary_key)
    form = ModuleForm(instance=module, user=request.user)

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module, user=request.user)
        if form.is_valid():
            form.save(commit=False)
            form.save_m2m()
            return redirect('home')

    context = {'form': form,
               'module': module}
    return render(request, 'module_form.html', context)


@login_required
def delete_module(request, primary_key):
    module = Module.objects.get(id=primary_key)

    if request.method == 'POST':
        module.delete()
        return redirect('home')

    context = {'object': module}
    return render(request, 'delete_module.html', context)


@login_required()
def toggle_favourites(request, module_id):
    module = Module.objects.get(id=module_id)
    student = Student.objects.get(user=request.user)
    if module in student.favourites.all():
        student.favourites.remove(module)
    else:
        student.favourites.add(module)
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def favourites(request):
    favourites = Student.objects.get(user=request.user).favourites.all()

    context = {'favourites': favourites}
    return render(request, 'favourites.html', context)


@login_required()
def sort(request, direction):
    global modules
    modules = Module.sort_modules_by_title(modules, direction)

    context = get_context_for_home(request)

    return render(request, 'home.html', context)


@login_required()
def filter(request):
    global modules
    semester = request.GET.get('semester')
    graduate_program = request.GET.get('program')
    specialisation_track = request.GET.get('track')
    credits = request.GET.get('credits')
    lecturer = request.GET.get('lecturer')

    if semester is not None:
        modules = Module.filter_modules_by_semester(semester)
    elif specialisation_track is not None:
        modules = Module.filter_modules_by_specialisation_track(specialisation_track)
    elif credits is not None:
        modules = Module.filter_modules_by_credits(credits)
    elif graduate_program is not None:
        modules = Module.filter_modules_by_graduate_program(graduate_program)
    elif lecturer is not None:
        modules = Module.filter_modules_by_lecturer(lecturer)
    else:
        modules = None

    context = get_context_for_home(request)

    return render(request, 'home.html', context)


@login_required()
def get_context_for_home(request):
    semesters = Semester.objects.all()
    specialisation_tracks = SpecialisationTrack.objects.all()
    credits = set(Module.objects.values_list('credits', flat=True))
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

    if student is not None:
        context['student'] = student

    return context


@login_required()
def get_student_for_context(request):
    try:
        return Student.objects.get(user=request.user)
    except:
        return None
