# Generated by Django 4.1.3 on 2022-11-23 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogposts',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='BlogApp.category'),
        ),
    ]
