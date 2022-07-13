#Recursos rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Recursos locales
from datos.models import datosModel
from datos.serializers import datosSerializer

#Para lectura de los sensores
import serial, time

# Create your views here.
class datosView(APIView):  
    def get_object(self, pk):
        try:
            return datosModel.objects.get(pk=pk)
        except datosModel.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        datos = self.get_object(pk)
        if datos != 0:
            datos = datosSerializer(datos)
            return Response(datos.data, status=status.HTTP_200_OK)
        return Response("No hay datos", status=status.HTTP_400_BAD_REQUEST)

    def saveData():
        esp = serial.Serial("COM3", 9600)
        valores = esp.readline().decode('utf-8').rstrip()            #No se ha probado el funcionamiento
        datos = valores.split()
        serializer = datosSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()