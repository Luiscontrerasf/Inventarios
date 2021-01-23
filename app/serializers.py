from .models import producto
from rest_framework import serializers

class productoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, min_length=3)
    
    def validate_nombre(self, value):
        existe = producto.objects.filter(nombre_iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")

        return value
    
    class Meta:
        model = producto
        fields = '__all__'