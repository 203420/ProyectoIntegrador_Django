from django.db import models

# Create your models here.
class datosModel(models.Model):
    temperatura = models.DecimalField(null=False)
    temperaturaS = models.DecimalField(null=False)
    humedad = models.DecimalField(null=False)
    humedadS = models.DecimalField(null=False)
    

