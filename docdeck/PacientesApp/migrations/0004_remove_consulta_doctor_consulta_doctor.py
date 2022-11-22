# Generated by Django 4.1.3 on 2022-11-19 15:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PacientesApp', '0003_alter_consulta_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='doctor',
        ),
        migrations.AddField(
            model_name='consulta',
            name='doctor',
            field=models.ManyToManyField(related_name='consulta', to=settings.AUTH_USER_MODEL),
        ),
    ]
