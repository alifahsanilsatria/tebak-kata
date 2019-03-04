from django.db import models

# Create your models here.

# menyimpan daftar kata
class Kata(models.Model):
	kata = models.CharField(max_length=256, unique=True)