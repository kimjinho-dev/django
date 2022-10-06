from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sighup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
