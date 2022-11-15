from django.db.models.signals import post_save
from .models import Paciente, HistoriaClinica
from django.dispatch import receiver

@receiver(post_save, sender=Paciente)
def create_profile(sender, instance, created, **kwargs):
    if created:
        HistoriaClinica.objects.create(user=instance)


@receiver(post_save, sender=Paciente)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()