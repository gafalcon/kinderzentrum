# -*- coding: utf-8 -*-
from django.db import models

class HistorialMadre(models.Model):
    enfermedades_previas = models.CharField("Indique si antes del embarazo ha sufrido algunas de las siguientes enfermedades",
                                        max_length=200, blank=True)
    enfermedades_durante_embarazo = models.CharField("Indique si durante el embarazo sufrió algunas de las siguientes enfermedades", max_length=256, blank=True)

    enfermedad_cronica = models.CharField("Indique algún tipo de enfermedad crónica", blank=True, max_length=100)
 
    defunciones_fetales = models.PositiveSmallIntegerField("¿Cuántas defunciones fetales ha tenido durante su vida?", default=0)

    hijos_nacidos_muertos = models.PositiveSmallIntegerField("Número de hijos nacidos muertos", default=0)
    hijos_nacidos_vivos = models.PositiveSmallIntegerField("Número de hijos nacidos vivos", default=0)
    embarazos = models.PositiveSmallIntegerField("número de embarazos", default=1)
    anticonceptivos = models.CharField(max_length=100, blank=True)

    enfermedades_antes_concepcion = models.CharField("¿Tuvo usted alguna enfermedad grave, dolencia, accidente o infección, antes de concebir a éste bebé", max_length=256, blank=True)


class Gestacion(models.Model):
    sentimientos = models.CharField(max_length=200)
    num_embarazo = models.PositiveSmallIntegerField()
    momento_desc_embarazo = models.PositiveSmallIntegerField()
    lugar_curso_prenatal = models.CharField(max_length=100, blank=True)
    carga_horaria = models.CharField(max_length=100, blank=True)
    nauseas_trimestre = models.SmallIntegerField()
    vacuna_tetano = models.BooleanField()
    comunicacion_bebe = models.CharField(max_length=500)
    

class Actividad_Gestacion(models.Model):
    tipo = models.SmallIntegerField()
    periodo = models.SmallIntegerField()
    gestacion = models.ForeignKey(Gestacion, on_delete=models.CASCADE)

class Situacion_Gestacion(models.Model):
    tipo = models.SmallIntegerField()
    periodo = models.SmallIntegerField()
    gestacion = models.ForeignKey(Gestacion, on_delete=models.CASCADE)

