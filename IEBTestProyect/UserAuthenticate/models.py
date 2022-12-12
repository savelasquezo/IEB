from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True, max_length=254)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username