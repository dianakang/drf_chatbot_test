from django.db import models

# Create your models here.
class Chatbot(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
