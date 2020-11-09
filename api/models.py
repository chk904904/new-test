from django.db import models

# Create your models here.


class Question1(models.Model):
    answer = models.CharField(max_length=200)


class Question2(models.Model):
    answer = models.CharField(max_length=200)
