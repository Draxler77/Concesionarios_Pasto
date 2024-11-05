from django.contrib import admin
from django.urls import path
from Catalogo import views
from django.conf import settings
from django.conf.urls.static import static

"""
URL configuration for Concesionario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('concesionario/', views.ConcesionarioListView.as_view(), name="concesionario-list"),
    path('vehiculo/', views.VehiculoListView.as_view(), name="vehiculo-list"),
    path('concesionario/<int:concesionario_id>/vehiculos/', views.VehiculoListView.as_view(), name="vehiculo-list"),

    path('vehiculo/<int:pk>/detail', views.VehiculoDetailView.as_view(), name="vehiculo-detail"),

    path('concesionario/create/', views.ConcesionarioCreateView.as_view(), name="concesionario-create"),
    path('vehiculo/create/', views.VehiculoCreateView.as_view(), name="vehiculo-create"),

    path('concesionario/<int:pk>/update/', views.ConcesionarioUpdateView.as_view(), name="concesionario-update"),
    path('concesionario/<int:pk>/delete/', views.ConcesionarioDeleteView.as_view(), name="concesionario-delete"),
    
    path('vehiculo/<int:pk>/update/', views.VehiculoUpdateView.as_view(), name="vehiculo-update"),
    path('vehiculo/<int:pk>/delete/', views.VehiculoDeleteView.as_view(), name="vehiculo-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)