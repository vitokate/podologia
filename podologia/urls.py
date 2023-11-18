from django.contrib import admin
from django.urls import path
from podo.views import CitaListView, agendar_cita

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citas/', CitaListView.as_view(), name='lista_citas'),
    path('agendar/', agendar_cita, name='agendar_cita'),
]

