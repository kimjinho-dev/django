from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.todos, name='todos'),
    path('new/', views.todos_new, name='todos_new'),
]