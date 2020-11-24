from django.db import models
from gsheets import mixins
from uuid import uuid4

# Create your models here.

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha",)
    dia = models.CharField(max_length=10)
    h_inicio = models.TimeField()
    h_fin = models.TimeField()
    grupo = models.CharField(max_length=10)
    profe = models.CharField(max_length=10)


class Classes(mixins.SheetSyncableMixin, models.Model):
    spreadsheet_id = '1aGYoYb_ZTXwB_1q9NcsCoPcKfsekRx5wvYB8DLYA4gI'
    model_id_field = 'id'
    range_values = '!A2:G'

    id = models.IntegerField(primary_key=True,)
    fecha = models.DateField(verbose_name="Fecha",)
    dia = models.CharField(max_length=10)
    h_inicio = models.TimeField()
    h_fin = models.TimeField()
    grupo = models.CharField(max_length=10)
    profe = models.CharField(max_length=10)
