from django.db import models

class Podologo(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos relevantes

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha_hora = models.DateTimeField()
    podologo = models.ForeignKey(Podologo, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100)  # O referencia a un modelo Cliente

    def __str__(self):
        return f"{self.fecha_hora} - {self.podologo}"
