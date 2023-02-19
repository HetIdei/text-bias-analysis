from django.db import models

# Create your models here.


class Answer(models.Model):
    name = models.CharField(max_length=50, blank=False)
    

class Text(models.Model):
    text = models.CharField(max_length=300, blank=False)
    answers = models.ManyToManyField(Answer)
