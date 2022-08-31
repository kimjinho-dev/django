import re
from django.shortcuts import render
from .models import Article


def index(request):
    article = Article.objects.all()
    context = {'articles': article}
    return render(request, 'articles/index.html')


def new(request):
    return render(request, 'articles/new.html')


# Create your views here.
