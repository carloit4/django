# Generated by Django 3.2.4 on 2022-12-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('identificacion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('Correo', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(blank=True, max_length=75)),
                ('Barrio', models.CharField(blank=True, max_length=75)),
                ('ciudad', models.CharField(blank=True, max_length=75)),
                ('departamento', models.CharField(blank=True, max_length=75)),
                ('pais', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
