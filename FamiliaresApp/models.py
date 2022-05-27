from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_lenght=10)
    apellido = models.CharField(max_lenght=10)
    edad = models.IntegerField(max_lenght=3)
    fechaNacimiento = models.CharField(max_lenght=10)
    