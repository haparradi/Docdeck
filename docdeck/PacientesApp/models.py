from django.db import models
from django.utils import timezone
ESTADO_CIVIL_CHOICE = [
    ('Casado/a', 'CASADO/A'),
    ('Soltero/a', 'SOLTERO/A'),
    ('Divociado/a','DIVORCIADO/A'),
    ('Viudo/a','VIUDO/A'),
]
# Create your models here.
class HistoriaClinica(models.Model):
    historia = models.TextField()
    pub_date = models.DateTimeField(blank=True, default=timezone.now)
    pass


class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()
    estado_civil = models.CharField(max_length=30, choices=ESTADO_CIVIL_CHOICE)
    religion = models.CharField(max_length=20)
    fehca_de_nacimiento = models.DateField()
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete = models.CASCADE, blank=True, null=True)
    