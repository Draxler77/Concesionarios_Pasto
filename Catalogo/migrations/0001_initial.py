# Generated by Django 5.1.2 on 2024-11-03 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concesionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('zona', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='concesionarios/')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('transmision', models.CharField(choices=[('Manual', 'Manual'), ('Automática', 'Automática')], max_length=10)),
                ('equipamiento', models.CharField(choices=[('Basico', 'Basico'), ('Full', 'Full')], max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('auto', models.ImageField(blank=True, null=True, upload_to='autos/')),
                ('info', models.CharField(max_length=1000)),
                ('concesionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='Catalogo.concesionario')),
            ],
        ),
    ]
