from django.contrib import admin
from django.urls import path
from miapp.views import CitaListView, agendar_cita  # Asegúrate de cambiar 'miapp' por el nombre real de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citas/', CitaListView.as_view(), name='lista_citas'),
    path('agendar/', agendar_cita, name='agendar_cita'),
]

