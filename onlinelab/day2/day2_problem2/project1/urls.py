from django.contrib import admin
from django.urls import path
from prices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prices/<str:thing>/<int:cnt>/', views.prices),
]
