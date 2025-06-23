
from django.shortcuts import render
from todos.models import Task


def home(request):
    task=Task.objects.filter(is_completed=False).order_by('-updatedAt')
    context={
        'tasks':task,
    }
    return render(request,'home.html',context)