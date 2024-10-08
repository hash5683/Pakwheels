# Generated by Django 4.2.11 on 2024-09-04 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0002_alter_carlisting_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='carlisting',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carlisting.carbrand'),
        ),
    ]
