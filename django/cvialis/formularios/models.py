from django.db import models

# Create your models here.
class ContratoEmpresas(models.Model):
    nomempresa = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(default=0)
    nombre_representante = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    valormensual = models.CharField(max_length=50)

    def __str__(self):
        return self.nomempresa

class ContratoProyectos(models.Model):
    nomempresa = models.CharField(max_length=100)
    rut = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(default=0)
    nombre_representante = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    fechainicio = models.DateField()
    fechatermino = models.DateField()
    nombre_proyecto = models.CharField(max_length=100)
    tipo_proyecto = models.CharField(max_length=50)
    valor_proyecto = models.IntegerField(default=0)
    observaciones = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_proyecto