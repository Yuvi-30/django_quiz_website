from django.db import models

# Create your models here.

class Rules(models.Model):
    details = models.CharField(max_length=500)
    