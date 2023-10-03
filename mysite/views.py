from django.shortcuts import render


def index(request: object) -> object:
    return render(request, "index.html")


def about(request: object) -> object:
    return render(request, "about.html")
