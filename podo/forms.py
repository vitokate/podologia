from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_paciente', 'apellidos_paciente', 'fecha_nacimiento', 'correo', 'podologo', 'fecha_cita', 'hora_cita']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_cita': forms.DateInput(attrs={'type': 'date'}),
            'hora_cita': forms.TimeInput(attrs={'type': 'time'}),
        }

