from django.db import models

# Create your models here.

class Terapia (models.Model):
    costo = models.IntegerField()
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre