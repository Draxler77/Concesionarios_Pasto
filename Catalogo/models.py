from django.db import models
from django.urls import reverse

class Concesionario(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='concesionarios/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
    
    def get_absolute_url(self):
        return reverse('concesionario-list')

class Vehiculo(models.Model):
    TRANSMISION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automática', 'Automática'),
    ]

    EQUIPAMIENTO_CHOICES = [
        ('Basico', 'Basico'),
        ('Full', 'Full'),
    ]

    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name='vehiculos')
    modelo = models.CharField(max_length=50)
    transmision = models.CharField(max_length=10, choices=TRANSMISION_CHOICES)
    equipamiento = models.CharField(max_length=100, choices=EQUIPAMIENTO_CHOICES)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    auto = models.ImageField(upload_to='autos/', null=True, blank=True)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.modelo} - {self.concesionario} - {self.precio} COP"
    
    