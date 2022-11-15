from django.db.models.signals import post_save
from .models import Paciente, HistoriaClinica
from django.dispatch import receiver

# @receiver(post_save, sender=Paciente)
# def create_historia(sender, instance, created, **kwargs):
#     if created:
#         HistoriaClinica.objects.create(paciente=instance)


# @receiver(post_save, sender=Paciente)
# def save_historia(sender, instance, **kwargs):
#     instance.historia.save()