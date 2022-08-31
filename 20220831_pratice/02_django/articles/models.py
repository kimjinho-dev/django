from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # PK는 자동으로 만들어진다


# Create your models here.
