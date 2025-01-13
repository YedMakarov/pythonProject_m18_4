from django.shortcuts import render


# from django.views.generic import TemplateView


# Create your views here.


def platform(request):
    return render(request, 'thrid_task/platform.html')


def games(request):
    return render(request, 'thrid_task/games.html')


def cart(request):
    return render(request, 'thrid_task/cart.html')
