from registro.modelos.medico_model import Medico
from table import Table
from table.columns import Column,CheckboxColumn

class PacienteTable(Table):
    id = Column(field='id')
    name = Column(field='nombres')
    Asistencia = CheckboxColumn(field='False');
    class Meta:
        model = Medico