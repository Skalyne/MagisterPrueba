from django.db import models
from gsheets import mixins
from uuid import uuid4
from django.urls import reverse

# Create your models here.

class Profesores(models.Model):
    DNI = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    movil = models.CharField(max_length=10, blank=True, null=True)

    def get_absolute_url(self):

        return reverse('index')


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha",)
    dia = models.CharField(max_length=10)
    h_inicio = models.TimeField()
    h_fin = models.TimeField()
    grupo = models.CharField(max_length=10)
    profe = models.ForeignKey(Profesores, on_delete=models.CASCADE)