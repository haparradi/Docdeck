from django.db import models
from django.utils import timezone
ESTADO_CIVIL_CHOICE = [
    ('Casado/a', 'CASADO/A'),
    ('Soltero/a', 'SOLTERO/A'),
    ('Divociado/a','DIVORCIADO/A'),
    ('Viudo/a','VIUDO/A'),
]
# Create your models here.


class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    documento = models.IntegerField()
    domicilio = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()
    estado_civil = models.CharField(max_length=30, choices=ESTADO_CIVIL_CHOICE)
    religion = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
class HistoriaClinica(models.Model):
    historia = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, default=timezone.now)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)