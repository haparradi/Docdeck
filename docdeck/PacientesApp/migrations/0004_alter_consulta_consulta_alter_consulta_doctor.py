# Generated by Django 4.1.3 on 2022-11-19 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PacientesApp', '0003_alter_historiaclinica_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='consulta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to=settings.AUTH_USER_MODEL),
        ),
    ]
