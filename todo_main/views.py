from django.http import HttpResponse
from django.shortcuts import render

from todo_app.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    return render(request=request, template_name='home.html', context=context)