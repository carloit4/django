from django.db import models

# Create your models here.
class Usuario(models.Model):
    identificacion=models.CharField(max_length=10, primary_key=True)
    nombres=models.CharField(max_length=100,)
    apellidos=models.CharField(max_length=100)
    correo=models.EmailField(blank=True)
    telefono=models.CharField(max_length=12)
    direccion=models.CharField(max_length=75, blank=True)
    barrio=models.CharField(max_length=75, blank=True)
    ciudad=models.CharField(max_length=75, blank=True)
    departamento=models.CharField(max_length=75, blank=True)
    pais=models.CharField(max_length=30)
    fecha_creacion=models.DateTimeField(auto_now_add=True)

