from django.db import models


# Create your models here.
class Notes(models.Model):
    heading = models.CharField(max_length=250, blank=True, unique=True)
    title = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)