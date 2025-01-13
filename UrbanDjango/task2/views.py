from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# def index_func_template(request):
#     return render(request, 'index_func_template.html')
#
#
# class index_class_template(TemplateView):
#     template_name = 'index_class_template.html'


def func_template(request):
    return render(request, 'func_template.html')


class class_template(TemplateView):
    template_name = 'class_template.html'
