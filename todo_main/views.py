
from django.shortcuts import render
from todos.models import Task


def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-updatedAt')
    completed_tasks=Task.objects.filter(is_completed=True).order_by('-updatedAt')
    context={
        'tasks':task,
        'completed_tasks':completed_tasks,
    }
    return render(request,'home.html',context)