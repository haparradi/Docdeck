from django import template
from PacientesApp.models import Consulta

register = template.Library()

@register.filter
def read(nuevas_consultas):
    print('hola')
    print(Consulta.objects.filter(read=False))
    return Consulta.objects.filter(read=False)