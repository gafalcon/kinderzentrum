from django.db import models
from asistencia.modelos.bebe_model import Bebe

class Cit(models.Model):
    ESTADO_CHOICES = (
        ("A", "Agendada"),
        ("S", "Asistio"),
        ("N", "No asistio"),
        ("C", "Cancelada")
    )
    """ Representa la cita del paciente """
    fecha_registro = models.DateTimeField( auto_now = True )
    fecha_cita = models.DateField( auto_now = False )
    hora_inicio = models.TimeField(auto_now=False)
    hora_fin = models.TimeField(auto_now=False)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2,default='A')
    indicaciones = models.CharField(max_length=256)
    #terapista_id = models.ForeignKey(Terapista, on_delete=models.CASCADE)
    bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE,default=1)


    def __str__(self):
        return str(self.bebe)
