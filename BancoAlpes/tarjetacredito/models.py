from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    # otros campos

class TarjetaCredito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    activa = models.BooleanField(default=True)
    cupo = models.FloatField()
    
    def __str__(self):
        return f'{self.tipo} - {self.cliente.nombre}'
