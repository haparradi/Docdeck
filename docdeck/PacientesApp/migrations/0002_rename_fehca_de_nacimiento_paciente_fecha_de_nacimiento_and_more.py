# Generated by Django 4.1.3 on 2022-11-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PacientesApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='fehca_de_nacimiento',
            new_name='fecha_de_nacimiento',
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='historia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
