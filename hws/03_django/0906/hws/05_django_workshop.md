# <사진>

## 1. Read

<img src="./image/1_read.jpg" width="300" height="300"/>

## 2. Create

<img src="./image/2_create.jpg" width="300" height="300"/>

## 3. Detail

<img src="./image/3_edit.jpg" width="300" height="300"/>

## 4. Update

<img src="./image/4_update.jpg" width="300" height="300"/>

<hr>

# <코드>

## 1. url

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

## 2. view

```python

from django.shortcuts import render, redirect

from articles.forms import ArticleForm
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context =  {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)



```

## 3. template

```html
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href=" {% url 'articles:create' %} ">create</a>
  <hr>
  {% for article in articles %}
    <p>제목 : {{article.title}} </p>
    <p>내용 : {{article.content}} </p>
    <a href=" {% url 'articles:detail' article.pk %} ">DETAIL</a>
    <hr>
    {% endfor %}
{% endblock  %}
```

```html
<!-- create.html -->
{% extends 'base.html' %}

{% block content %}
<h1>create</h1>
<form action=" {% url 'articles:create' %} " method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit">
</form>
<a href=" {% url 'articles:index' %} ">홈으로 돌아가기</a>

{% endblock  %}
```

```html
<!-- detail.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL</h1>
  <hr>
  <p>제목 : {{article.title}} </p>
  <p>내용 : {{article.content}} </p>
  <p>작성시간 : {{article.created_at}} </p>
  <p>수정시간 : {{article.updated_at}} </p>
  <form action=" {% url 'articles:delete' article.pk %} " method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <form action=" {% url 'articles:update' article.pk %} " method="GET">
    {% csrf_token %}
    <input type="submit" value="UPDATE">
  </form>
  <a href=" {% url 'articles:index' %} ">INDEX</a>

{% endblock  %}



```

```html
<!-- update.html -->
{% extends 'base.html' %}

{% block content %}
<h1>UPDATE</h1>
<form action=" {% url 'articles:update' article.pk %} " method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit">
</form>
<a href=" {% url 'articles:index' %} ">홈으로 돌아가기</a>

{% endblock  %}
```

## 4. model

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

## 5. forms

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
```
