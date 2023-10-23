from django.db import models

# Create your models here
## usuarios registrados
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
## Interesados en consultorías
class Interesado(models.Model):
    nombre = models.CharField(max_length=40, default='nombre')
    apellido = models.CharField(max_length=20, default='apellido')
    email = models.EmailField(max_length=40, default='mail')
    organizacion = models.CharField(max_length=40, default='org')
    cuit = models.CharField(max_length=40, default='cuit')
    servicio = models.CharField(max_length=40, default='consultorias varias')
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Organización: {self.organizacion} - CUIT: {self.cuit} - Servicio: {self.servicio}"
## Talleres disponibles
class Taller(models.Model):
    taller = models.CharField(max_length=40, default='Otros')
    comision = models.CharField(max_length=40, default='1234')
    def __str__(self):
        return f"Taller: {self.taller} - Comisión: {self.comision}" 
## Interesados en talleres
class InteresadoTalleres(models.Model):
    nombre = models.CharField(max_length=40, default='faltante')
    taller = models.CharField(max_length=40, default='varios')
    def __str__(self):
        return f"Nombre: {self.nombre} - Taller: {self.taller}" 