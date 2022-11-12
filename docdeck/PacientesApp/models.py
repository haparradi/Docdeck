from django.db import models
from django.utils import timezone

# Create your models here.
class HistoriaClinica(models.Model):
    historia = models.TextField()
    pub_date = models.DateTimeField(blank=True, default=timezone.now)
    pass


class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()
    obra_social = models.CharField(max_length=30)
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete = models.CASCADE, blank=True, null=True)
    pass