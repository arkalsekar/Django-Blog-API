from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=100, blank=True, default="admin")
    title = models.CharField(max_length=100, blank=True, default="")
    content = models.CharField(max_length=500, blank=True, default="")
    tags = models.CharField(max_length=500, blank=True, default="")