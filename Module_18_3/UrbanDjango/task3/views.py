from django.shortcuts import render


# Create your views here.
def class_template(request):
    return render(request, "class_template.html")


def func_template(request):
    return render(request, "func_template.html")


def class_module(request):
    return render(request, "module.html")


def func_platform(request):
    return render(request, "platform.html")


def func_korzina(request):
    return render(request, "cart.html")


def func_magazin(request):
    return render(request, "games.html")
