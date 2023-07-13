from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nombre_empresa = models.CharField(max_length=40)
    email = models.EmailField()


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

class producto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=40)
    bars_code = models.IntegerField(null=True, blank=True)
    descripcion_producto = models.CharField(max_length=200)
    stock_producto = models.IntegerField()
    precio_producto = models.FloatField()
    imagen_producto = models.ImageField(upload_to='productos/', blank=True, null=True)



    