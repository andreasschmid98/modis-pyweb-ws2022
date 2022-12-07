from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Module
from .forms import ModuleForm


@login_required
def home(request):
    search_query = request.GET.get('q') if request.GET.get('q') is not None else ''
    modules = Module.filter_modules_by_search_query(search_query)
    module_count = modules.count()

    context = {'modules': modules,
               'module_count': module_count}
    return render(request, 'home.html', context)


@login_required
def module(request, primary_key):
    module = Module.objects.get(id=primary_key)
    context = {'module': module}
    return render(request, 'module.html', context)


@login_required
def create_module(request):
    form = ModuleForm(user=request.user)

    if request.method == 'POST':
        form = ModuleForm(request.POST, user=request.user)
        if form.is_valid():
            form.save(user=request.user)
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
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'module_form.html', context)


@login_required
def delete_module(request, primary_key):
    module = Module.objects.get(id=primary_key)

    if request.method == 'POST':
        module.delete()
        return redirect('home')

    context = {'object': module}
    return render(request, 'delete.html', context)
