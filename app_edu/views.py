from django.shortcuts import render, redirect
from django.http import Http404
from .models import Module

def module_list(request):
    modules = Module.objects.all()
    context = {'modules': modules}
    return render(request, 'module_list.html', context)

def module_create(request):
    if request.method == 'POST':
        serial_number = request.POST['serial_number']
        name = request.POST['name']
        description = request.POST['description']
        Module.objects.create(serial_number=serial_number, name=name, description=description)
        return redirect('module_list')
    else:
        return render(request, 'module_form.html')

def module_update(request, pk):
    try:
        module = Module.objects.get(pk=pk)
    except Module.DoesNotExist:
        raise Http404("Module does not exist")

    if request.method == 'POST':
        module.serial_number = request.POST['serial_number']
        module.name = request.POST['name']
        module.description = request.POST['description']
        module.save()
        return redirect('module_list')
    else:
        context = {'module': module}
        return render(request, 'module_form.html', context)

def module_delete(request, pk):
    try:
        module = Module.objects.get(pk=pk)
    except Module.DoesNotExist:
        raise Http404("Module does not exist")

    if request.method == 'POST':
        module.delete()
        return redirect('module_list')
    else:
        context = {'module': module}
        return render(request, 'module_confirm_delete.html', context)
