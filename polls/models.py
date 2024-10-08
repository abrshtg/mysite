import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
