from django.conf import settings
from django.db import models


class Todo(models.Model):
    title = models.TextField()
    completed = models.BooleanField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)