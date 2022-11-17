from LoginApp.models import Doctor
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
    documento = models.CharField(null=True, blank=True, max_length=20)
    domicilio = models.CharField(null=True, blank=True, max_length=20)
    telefono = models.CharField(null=True, blank=True, max_length=20)
    email = models.EmailField()
    estado_civil = models.CharField(max_length=30, choices=ESTADO_CIVIL_CHOICE)
    religion = models.CharField(max_length=20)
    fecha_de_nacimiento = models.DateField()
    doctor = models.ManyToManyField(Doctor, related_name='paciente')
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
class HistoriaClinica(models.Model):
    historia = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, default=timezone.now)
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, default=None,)
    
    def __str__(self):
        return f'{self.paciente}'
    
class Consulta(models.Model):
    nombre_apellido = models.CharField(max_length=40)
    email = models.EmailField()
    consulta = models.TextField()
    read = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    