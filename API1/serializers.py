from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('identificacion','nombres','apellidos','correo','telefono','direccion','barrio','ciudad','departamento', 'pais','fecha_creacion')
        read_only_fields=('fecha_creacion',)
        