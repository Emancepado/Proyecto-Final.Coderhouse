from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nombre_empresa = models.CharField(max_length=40)
    email = models.EmailField()


