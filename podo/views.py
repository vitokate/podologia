from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Cita
from .forms import CitaForm
from django.contrib import messages
from django.utils import timezone
import pytz

class CitaListView(ListView):
    model = Cita
    template_name = 'lista_citas.html'

def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            # Ajustar a la zona horaria de Chile
            hora_chilena = pytz.timezone('Chile/Continental')
            cita.fecha_cita = cita.fecha_cita.astimezone(hora_chilena)
            cita.hora_cita = cita.hora_cita.astimezone(hora_chilena)

            # Verificar si ya existe una cita para ese podólogo en la fecha y hora especificadas
            if not Cita.objects.filter(podologo=cita.podologo, fecha_cita=cita.fecha_cita, hora_cita=cita.hora_cita).exists():
                cita.save()
                messages.success(request, 'Cita agendada con éxito.')
                return redirect('alguna_url')
            else:
                messages.error(request, 'El podólogo seleccionado ya tiene una cita en ese horario.')
    else:
        form = CitaForm()

    return render(request, 'agendar_cita.html', {'form': form})


