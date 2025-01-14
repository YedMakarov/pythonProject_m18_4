from django.shortcuts import render


# from django.views.generic import TemplateView


# Create your views here.


def platform(request):
    return render(request, 'thrid_task/platform.html')


# def games(request):
#     return render(request, 'thrid_task/games.html')
def games(request):
    game1 = 'Atomic Heart '
    game2 = 'Cyberpunr 2077 '
    game3 = 'PayDay 2 '
    context = {
        'game1': game1,
        'game2': game2,
        'game3': game3
    }
    return render(request, 'thrid_task/games.html', context)


def cart(request):
    return render(request, 'thrid_task/cart.html')
