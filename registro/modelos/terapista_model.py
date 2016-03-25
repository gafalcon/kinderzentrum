from __future__ import unicode_literals

from django.db import models

class Terapista(models.Model):
    """ Representa el terapista del paciente """
    GRUPO_SANGUINEO_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"), 
        ("AB-", "AB-")        
    )
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=256)
    telefonos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField("fecha de nacimiento")
    grupo_sanguineo = models.CharField("grupo sanguineo",
                                        choices=GRUPO_SANGUINEO_CHOICES,
                                        max_length=4)
    especialidad = models.CharField(max_length=256)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres

