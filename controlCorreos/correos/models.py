from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Residencia(models.Model):
    numero = models.IntegerField(primary_key=True)
    dueño = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)
    mail =models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.numero)

ESTADO_CHOICES = (("REC","Recibido"),("ENT","Entregado"))

class Correspondencia(models.Model):
    id_correo = models.IntegerField(primary_key=True)
    fecha_recepcion = models.DateField()
    conserje = models.ForeignKey(User, on_delete=models.CASCADE)
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    estado = models.CharField(max_length=9,choices=ESTADO_CHOICES,default="REC")
    numero = models.ForeignKey("Residencia",null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.destinatario+" del "+str(self.numero)

    def datepublished(self):
        return self.fecha_recepcion.strftime('%B %d %Y')