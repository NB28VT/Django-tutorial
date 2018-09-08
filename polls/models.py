# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # Some fields require args, such as max_length here
    question_text = models.CharField(max_length=200)
    # "date published" argument here is human readable name (optional). Instead of "pub_date"
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # These are field classes:
    # var is column name, will be used in app but also column name in db
    # Note foreign key relationship. question_id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
