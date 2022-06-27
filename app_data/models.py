from django.db import models

# Create your models here.

class Presidente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    asume_cargo = models.DateField()
    deja_cargo = models.DateField()
    partido = models.CharField(max_length=60)
    constitucional = models.BooleanField()

class Ministro(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    asume_cargo = models.DateField()
    deja_cargo = models.DateField()
    cartera = models.CharField(max_length=60)

class Partido(models.Model):
    nombre = models.CharField(max_length=60)
    fundacion = models.DateField()
    antiguedad = models.IntegerField()