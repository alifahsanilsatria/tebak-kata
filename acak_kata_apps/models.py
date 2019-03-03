from django.db import models

# Create your models here.
class Kata(models.Model):
	kata = models.CharField(max_length=256, unique=True)