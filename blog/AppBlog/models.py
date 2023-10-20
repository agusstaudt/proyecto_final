from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

class Interesado(models.Model):
    nombre = models.CharField(max_length=40, default='nombre')
    apellido = models.CharField(max_length=20, default='apellido')
    email = models.EmailField(max_length=40, default='mail')
    organizacion = models.CharField(max_length=40, default='org')
    cuit = models.CharField(max_length=40, default='cuit')

class Consultoria(models.Model):
    servicio = models.CharField(max_length=40)