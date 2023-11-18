from django.shortcuts import render, redirect  # Agregado redirect aquí
from .models import Cita
from .forms import CitaForm
from django.views.generic import ListView
from django.urls import reverse_lazy

class CitaListView(ListView):
    model = Cita
    template_name = 'podo/lista_citas.html'

    def get_queryset(self):
        # Aquí puedes modificar el queryset para filtrar por día, mes, año
        # Por ahora, simplemente devuelve todas las citas
        return Cita.objects.all()

# Agregamos una indentación adecuada para la función agendar_cita
def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()

    return render(request, 'podo/agendar_cita.html', {'form': form})
