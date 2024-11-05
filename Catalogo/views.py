from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Catalogo.models import Concesionario, Vehiculo
from django.contrib import messages

class HomeView(TemplateView):
    template_name = 'base.html'

#Listas
class ConcesionarioListView(ListView):
    model = Concesionario
    template_name = 'catalogo/Concesionario_list.html'
    context_object_name = 'object_list' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'catalogo/vehiculo_list.html'

    def get_queryset(self):
        concesionario_id = self.kwargs.get('concesionario_id')
        if concesionario_id:
            return Vehiculo.objects.filter(concesionario_id=concesionario_id)
        return Vehiculo.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concesionario_id = self.kwargs.get('concesionario_id')
        if concesionario_id:
            try:
                context['concesionario'] = Concesionario.objects.get(id=concesionario_id)
            except Concesionario.DoesNotExist:
                context['concesionario'] = None
        return context

#Detalles
class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'catalogo/vehiculo_detail.html'

#Crear
class ConcesionarioCreateView(CreateView):
    model = Concesionario
    template_name = 'catalogo/concesionario_form.html'
    fields = '__all__'
    success_url = reverse_lazy('concesionario-list')
        
class VehiculoCreateView(CreateView):
    model = Vehiculo
    template_name = 'catalogo/vehiculo_form.html'
    fields = '__all__'
    success_url = reverse_lazy('concesionario-list')

#Actualizar
class ConcesionarioUpdateView(UpdateView):
    model = Concesionario
    fields = '__all__'
    template_name = 'catalogo/concesionario_update.html'
    success_url = reverse_lazy('concesionario-list')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    fields = '__all__'
    template_name = 'catalogo/vehiculo_update.html'
    success_url = reverse_lazy('concesionario-list')

#Eliminar
class ConcesionarioDeleteView(DeleteView):
    model = Concesionario
    success_url = reverse_lazy('concesionario-list')
    
    def delete(self, request, *args, **kwargs):
        Concesionario = self.get_object()
        messages.success(request, f'El equipo "{Concesionario.name}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('concesionario-list')
    
    def delete(self, request, *args, **kwargs):
        Vehiculo = self.get_object()
        messages.success(request, f'El vehículo "{Vehiculo.modelo}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

