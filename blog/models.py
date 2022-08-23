from django.db import models

class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    date = models.DateField()
    description = models.CharField(max_length=100)
