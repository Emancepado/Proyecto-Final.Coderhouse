from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    id = models.AutoField(primary_key=True)
    bars_code = models.IntegerField(null=True, blank=True)
    nombre_producto = models.CharField(max_length=40)
    descripcion_producto = models.CharField(max_length=200)
    stock_producto = models.IntegerField()
    precio_producto = models.FloatField()
    imagen_producto = models.ImageField(upload_to='productos', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.nombre_producto


class Venta(models.Model):
    Producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def clean(self):
        super().clean()
        if self.cantidad > self.producto.stock_producto:
            raise ValidationError("La cantidad excede el stock disponible del producto.")