import re
from django.shortcuts import render


def calculatoes(request):
    return render(request, 'calculatoes.html')


def result(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    context = {
        'first': first,
        'second': second,
        'minus': first - second,
        'multiply': first * second,
        'divide': first / second if second else 0,
    }
    return render(request, 'result.html', context)


# Create your views here.
