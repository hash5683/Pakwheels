# Generated by Django 4.2.11 on 2024-09-04 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlisting',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
