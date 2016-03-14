# -*- coding: utf-8 -*-

from django.db import models


class AlimentacionCostumbres(models.Model):
    """Alimentación y Costumbres"""
    tiempo_leche_materna = models.CharField("¿Cuánto tiempo recibió leche materna?", max_length=25)
    motivo_suspencion_lactancia = models.CharField("¿Por qué suspendió la leche materna?", max_length=100)
    
 
