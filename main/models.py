from django.db import models


class Main(models.Model):
    img = models.ImageField(upload_to="main/")
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=120)
    link = models.CharField(max_length=255)