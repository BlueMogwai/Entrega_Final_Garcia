from django.contrib import admin

from .models import Grupo, Clase, Reserva, Avatar

# Register your models here.

admin.site.register(Grupo)
admin.site.register(Clase)
admin.site.register(Reserva)
admin.site.register(Avatar)