from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return JsonResponse({'status': 'success'})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status': 'success'})

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return JsonResponse({'status': 'success'})
