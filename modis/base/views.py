from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ModuleForm
from .models import Module, Student
from .utils import get_context_for_home, get_student_for_context

# Store modules for the views in a global variable
modules = Module.objects.all()


@login_required
def home(request):
    global modules
    search_query = request.GET.get('q') if request.GET.get('q') is not None else ''
    modules = Module.filter_modules_by_search_query(search_query)
    context = get_context_for_home(modules, request)
    return render(request, 'home.html', context)


@login_required
def module(request, pk):
    module = Module.objects.get(id=pk)
    context = {'module': module}

    # Add logged-in student to the context (only if a user of type STUDENT ist logged in)
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
            form.save(user=request.user)
            form.save_m2m()
            return redirect('home')

    context = {'form': form}
    return render(request, 'module_form.html', context)


@login_required
def update_module(request, pk):
    module = Module.objects.get(id=pk)
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
def delete_module(request, pk):
    module = Module.objects.get(id=pk)

    if request.method == 'POST':
        module.delete()
        return redirect('home')

    context = {'object': module}
    return render(request, 'delete_module.html', context)


@login_required()
def toggle_favourites(request, pk):
    module = Module.objects.get(id=pk)
    student = Student.objects.get(user=request.user)

    # Add module to favourites if it is not in favourites, else remove
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
    context = get_context_for_home(modules, request)
    return render(request, 'home.html', context)


@login_required()
def filter(request):
    global modules

    # Get all possible filter criteria
    semester = request.GET.get('semester')
    graduate_program = request.GET.get('program')
    specialisation_track = request.GET.get('track')
    credits = request.GET.get('credits')
    lecturer = request.GET.get('lecturer')

    # Check if one filter is selected
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

    context = get_context_for_home(modules, request)
    return render(request, 'home.html', context)
