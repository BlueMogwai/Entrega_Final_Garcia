from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Size(models.Model):
    duo = "duo"
    trio = "trio"
    cuarteto = "cuarteto"
    combo = "combo"

    size_choices = [
        (duo, "duo"),
        (trio, "trio"),
        (cuarteto, "cuarteto"),
        (combo, "combo"),
    ]

    size = models.CharField(max_length=10, choices=size_choices)


class Tipo(models.Model):
    instrumental = "instrumental"
    con_voz = "convoz"

    tipo_choices = [
        (instrumental, "Grupo instrumental"),
        (con_voz, "Grupo con vocalista"),
    ]

    tipo = models.CharField(max_length=20, choices=tipo_choices)


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    size = models.CharField(
        max_length=20,
        choices=Size.size_choices,
        default=Size.combo
        )
    tipo = models.CharField(
        max_length=20,
        choices=Tipo.tipo_choices,
        default=Tipo.instrumental
        )
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nombre}"

class Clase(models.Model):
    nombre = models.CharField(max_length=250)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='grupo')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

class Reserva(models.Model):
    nombre = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="reservas")
    instrumento = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    experiencia = models.BooleanField(default=True)
    presentacion = models.TextField(max_length=500)
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)

    def get_experiencia_display(self):
        return "Si" if self.experiencia else "No"

    def __str__(self):
        return f"¡{self.nombre} ha reservado la clase {self.clase}!"