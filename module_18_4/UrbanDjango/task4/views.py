from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Template(TemplateView):
    template_name = "menu.html"


def func_platform(request):
    return render(request, "platform.html")


def func_magazin(request):
    digits_games = {'first': "Atomic Heart", 'second': 'Cyberpunk 2077'}
    items = digits_games.items()
    context = {
        'items': items
    }
    return render(request, "games.html", context)


def func_korzina(request):
    return render(request, "cart.html")