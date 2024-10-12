from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm
import json

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def update_task_status(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')

        try:
            task = Task.objects.get(id=task_id)
            task.status = status
            task.save()
            return JsonResponse({'message': 'Task status!'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not fined.'}, status=404)
    return JsonResponse({'error': 'Not correct.'}, status=400)
