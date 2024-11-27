from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Catalogo.models import Concesionario, Vehiculo
from django.contrib import messages

class HomeView(TemplateView):
    template_name = 'base.html'

class ConcesionarioListView(ListView):
    model = Concesionario
    template_name = 'catalogo/Concesionario_list.html'
    context_object_name = 'object_list' 
    paginate_by = 6

    def get_queryset(self):
        queryset = Concesionario.objects.all()
        search_query = self.request.GET.get('search')
        
        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)
        
        return queryset

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'catalogo/vehiculo_list.html'
    context_object_name = 'object_list'
    paginate_by = 6

    def get_queryset(self):
        queryset = Vehiculo.objects.all()
        concesionario_id = self.kwargs.get('concesionario_id')
        search_query = self.request.GET.get('search')
        
        if concesionario_id:
            queryset = queryset.filter(concesionario_id=concesionario_id)
        
        if search_query:
            queryset = queryset.filter(modelo__icontains=search_query)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concesionario_id = self.kwargs.get('concesionario_id')
        if concesionario_id:
            context['concesionario'] = Concesionario.objects.get(id=concesionario_id)
        return context

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'catalogo/vehiculo_detail.html'

class ConcesionarioCreateView(CreateView):
    model = Concesionario
    fields = '__all__'
    template_name = 'catalogo/concesionario_form.html'
    success_url = reverse_lazy('concesionario-list')

class VehiculoCreateView(CreateView):
    model = Vehiculo
    fields = '__all__'
    success_url = reverse_lazy('concesionario-list')

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

class ConcesionarioDeleteView(DeleteView):
    model = Concesionario
    success_url = reverse_lazy('concesionario-list')
    
    def delete(self, request, *args, **kwargs):
        concesionario = self.get_object()
        messages.success(request, f'El concesionario "{concesionario.nombre}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    success_url = reverse_lazy('concesionario-list')
    
    def delete(self, request, *args, **kwargs):
        vehiculo = self.get_object()
        messages.success(request, f'El vehículo "{vehiculo.modelo}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)