# Generated by Django 4.1.3 on 2022-11-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0004_doctor_especialidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
