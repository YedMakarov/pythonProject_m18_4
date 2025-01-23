from django.shortcuts import render


# from django.views.generic import TemplateView


# Create your views here.


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    game1 = 'Atomic Heart '
    game2 = 'Cyberpunr 2077 '
    game3 = 'PayDay 2 '
    context = {'games': [game1, game2, game3]}
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
