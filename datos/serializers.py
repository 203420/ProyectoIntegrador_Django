from rest_framework import serializers

from datos.models import datosModel

class datosSerializer(serializers.ModelSerializer):
    class Meta:
        model = datosModel
        fields = ('__all__')