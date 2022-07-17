from datetime import timezone
from pytz import timezone
from django.utils import timezone
from django.db import models

# Create your models here.
class datosModel(models.Model):
    nivelA = models.DecimalField(null=False)
    humedadS = models.DecimalField(null=False)
    temperatura = models.DecimalField(null=False)
    humedad = models.DecimalField(null=False)
    fecha = models.DateTimeField(default=timezone.now)
    

