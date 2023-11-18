from django.db import models

PODOLOGOS_CHOICES = [
    ('Podologo 1', 'Podólogo 1'),
    ('Podologo 2', 'Podólogo 2'),
    ('Podologo 3', 'Podólogo 3'),
    ('Podologo 4', 'Podólogo 4'),
    ('Podologo 5', 'Podólogo 5'),
]

class Cita(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellidos_paciente = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(blank=True, null=True)  # Opcional
    podologo = models.CharField(max_length=50, choices=PODOLOGOS_CHOICES)

    # Otros campos necesarios...

