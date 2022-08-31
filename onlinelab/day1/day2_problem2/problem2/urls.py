from django.contrib import admin
from django.urls import path
from calculatoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculatoes/', views.calculatoes),
    path('result/', views.result),
]
