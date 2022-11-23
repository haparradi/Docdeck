from django import template
from PacientesApp.models import Consulta

register = template.Library()

@register.filter
def read(nuevas_consultas):
    return Consulta.objects.filter(read=False)