from django.http import HttpResponse, JsonResponse
from .models import Project, Task  # Importamos el modelo de la base de datos.
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("Index page")


def hello(request, age: int):
    return HttpResponse(f"<h1>Hello! You're {age} years old</h1>")


def about(request):
    return HttpResponse("About")


def info(request, username: str, age: int):
    return HttpResponse(f"<h1>Hello {username}! You're {age} years old")


def projects(request):
    p = list(Project.objects.values())
    return JsonResponse(p, safe=False)


def tasksById(request, id: int):
    t = Task.objects.get(id=id)
    return HttpResponse(f"task title: {t.title}")


def tasksByTitle(request, title: str):
    t = get_object_or_404(Task, title=title)
    return HttpResponse(f"task id: {t.id}")
