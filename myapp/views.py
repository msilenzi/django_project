from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page")


def hello(request, age: int):
    return HttpResponse(f"<h1>Hello! You're {age} years old</h1>")


def about(request):
    return HttpResponse("About")


def info(request, username: str, age: int):
    return HttpResponse(f"<h1>Hello {username}! You're {age} years old")
