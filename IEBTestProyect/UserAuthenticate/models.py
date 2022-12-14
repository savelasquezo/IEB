from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    pass

class Proyect(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nmproy = models.CharField(max_length=64)
    typroy = models.CharField(max_length=64)
