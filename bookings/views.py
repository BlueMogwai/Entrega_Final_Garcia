from .models import Grupo, Clase, Reserva
# from .forms import UserEditForm, JuegoSearchForm, SistemaSearchForm
from django import forms
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")

# -----------------------------------------------------------------------------
# CRUD: CLASES
# -----------------------------------------------------------------------------



class ClaseListView(LoginRequiredMixin, ListView):
    model = Clase
    template_name = "bookings/vbc/clase_list.html"
    context_object_name = "todas_las_clases"


class ClaseDetailView(LoginRequiredMixin, DetailView):
    model = Clase
    template_name = "bookings/vbc/clase_detail.html"
    context_object_name = "detalle_clase"


class ClaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Clase
    template_name = "bookings/vbc/clase_confirm_delete.html"
    success_url = reverse_lazy("clase-list")


class ClaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Clase
    template_name = "bookings/vbc/clase_form.html"
    fields = ["nombre", "disponible", "capacidad", "grupo", "descripcion"]
    context_object_name = "clase"
    success_url = reverse_lazy("clase-list")


class ClaseCreateView(LoginRequiredMixin, CreateView):
    model = Clase
    template_name = "bookings/vbc/clase_form.html"
    fields = ["nombre", "disponible", "capacidad", "grupo", "descripcion"]
    success_url = reverse_lazy("clase-list")