from django.contrib import admin
from django.urls import path
from fruits import views

urlpatterns = [path('admin/', admin.site.urls), path('fruits/', views.fruits)]
