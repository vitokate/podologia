from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Cita
from .forms import CitaForm
from django.contrib import messages
import pytz
from datetime import datetime

class CitaListView(ListView):
    model = Cita
    template_name = 'lista_citas.html'

    def get_queryset(self):
        fecha = self.request.GET.get('fecha')
        if fecha:
            try:
                fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
                return Cita.objects.filter(fecha_cita=fecha)
            except ValueError:
                pass
        return Cita.objects.all()

def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            # Ajustar a la zona horaria de Chile
            hora_chilena = pytz.timezone('Chile/Continental')
            # cita.fecha_cita es un objeto date, no necesita ajuste de zona horaria
            # cita.hora_cita es un objeto time, no necesita ajuste de zona horaria

            # Verificar si ya existe una cita para ese podólogo en la fecha y hora especificadas
            if not Cita.objects.filter(podologo=cita.podologo, fecha_cita=cita.fecha_cita, hora_cita=cita.hora_cita).exists():
                cita.save()
                messages.success(request, 'Cita agendada con éxito.')
                return redirect('lista_citas')
            else:
                messages.error(request, 'El podólogo seleccionado ya tiene una cita en ese horario.')
    else:
        form = CitaForm()

    return render(request, 'agendar_cita.html', {'form': form})
