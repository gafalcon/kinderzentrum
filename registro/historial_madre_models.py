# -*- coding: utf-8 -*-
from django.db import models

class Historial_madre(models.Model):
    
    perdidas_gestacionales = models.IntegerField()
    hijos_muertos = models.BooleanField()
    num_hijos_nacidos_muertos = models.SmallIntegerField()
    num_hijos_nacidos_vivos = models.SmallIntegerField()
    enfermedades_previas = models.CharField("¿Enfermedad antes de concebir al bebé?",
                                            max_length=200, blank=True)
    anticonceptivos = models.CharField(max_length=100, blank=True)

class Enfermedad_Madre(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_desarrollo = models.CharField(max_length=25)
    historial_madre = models.ForeignKey(Historial_madre, on_delete=models.CASCADE)



class Gestacion(models.Model):
    sentimientos = models.CharField(max_length=200)
    fecha_embarazo = models.CharField(max_length=100)
    num_embarazo = models.SmallIntegerField()
    nauseas_trimestre = models.SmallIntegerField()
    vacuna_tetano = models.BooleanField()
    comunicacion_bebe = models.CharField(max_length=500)
    curso_prenatal = models.BooleanField()
    

class Actividad_Gestacion(models.Model):
    tipo = models.SmallIntegerField()
    periodo = models.SmallIntegerField()
    historial_madre = models.ForeignKey(Historial_madre, on_delete=models.CASCADE)

class Situacion_Gestacion(Actividad_Gestacion):
    pass
