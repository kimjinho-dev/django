from random import choices
from secrets import choice
from django.db import models

class Vote(models.Model):
    question = models.CharField(max_length=50)
    left_player = models.CharField(max_length=50)
    right_player = models.CharField(max_length=50)

class Comment(models.Model):
    question = models.ForeignKey(Vote, on_delete=models.CASCADE)
    team_Choices = (('왼쪽','왼쪽'),('오른쪽','오른쪽'))
    team = models.CharField(max_length=50,choices=team_Choices)
    content = models.TextField()
