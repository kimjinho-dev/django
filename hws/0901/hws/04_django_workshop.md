# 사진

## 1. Read

<img src="01_Read.png" width="300" height="300"/>

## 2. Create

<img src="02_Create.png" width="300" height="300"/>

## 3. Detail

<img src="03_Detail.png" width="300" height="300"/>

## 4. Update

<img src="04_Update.png" width="300" height="300"/>

## 5. delete

<img src="05_delete_01.png" width="300" height="300"/>
<img src="05_delete_02.png" width="300" height="300"/>

<hr>

# 코드

## url

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```

## view

```python

from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')

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

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')

```

## template

```html
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
<h1>UPDATE</h1>
<form action=" {% url 'articles:update' article.pk %} " method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" id="title" name="title" value="{{article.title}}">
  <br>
  <div class="ps-0 md-0" style="height:300px">
    <label for="content">CONTENT:</label>
    <textarea name="content" id="content" cols="30" rows="10"> {{article.content}} </textarea>
  </div>
  <input type="submit">
</form>
<a href=" {% url 'articles:index' %} ">홈으로 돌아가기</a>

{% endblock  %}
```

```html
<!-- new.html -->
{% extends 'base.html' %}

{% block content %}
<h1>NEW</h1>
<form action=" {% url 'articles:create' %} " method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" id="title" name="title">
  <br>
  <div class="ps-0 md-0" style="height:300px">
    <label for="content" class="">CONTENT:</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
  </div>
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
  <form action=" {% url 'articles:edit' article.pk %} " method="POST">
    {% csrf_token %}
    <input type="submit" value="UPTATE">
  </form>
  <a href=" {% url 'articles:index' %} ">INDEX</a>

{% endblock  %}
```

```html
<!-- edit.html -->

{% extends 'base.html' %}

{% block content %}
<h1>UPDATE</h1>
<form action=" {% url 'articles:update' article.pk %} " method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" id="title" name="title" value="{{article.title}}">
  <br>
  <div class="ps-0 md-0" style="height:300px">
    <label for="content">CONTENT:</label>
    <textarea name="content" id="content" cols="30" rows="10"> {{article.content}} </textarea>
  </div>
  <input type="submit">
</form>
<a href=" {% url 'articles:index' %} ">홈으로 돌아가기</a>

{% endblock  %}
```

## model

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```