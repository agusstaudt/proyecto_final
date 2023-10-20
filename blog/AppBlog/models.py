from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

class Interesado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    organizacion = models.CharField(max_length=40)
    cuit = models.CharField(max_length=40)
    comentario_interes = models.CharField(max_length=200)

# class Profesor(models.Model):
#     nombre = models.CharField(max_length=40)
#     apellido = models.CharField(max_length=20)
#     email = models.EmailField(max_length=40)
