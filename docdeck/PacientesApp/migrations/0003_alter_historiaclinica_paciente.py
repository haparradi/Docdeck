# Generated by Django 4.1.3 on 2022-11-16 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PacientesApp', '0002_rename_fehca_de_nacimiento_paciente_fecha_de_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='paciente',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='PacientesApp.paciente'),
        ),
    ]