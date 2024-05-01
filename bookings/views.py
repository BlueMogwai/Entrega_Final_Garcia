from .models import Grupo, Clase, Reserva, Avatar
from .forms import UserEditForm
from .forms import ClaseSearchForm, GrupoSearchForm, AvatarCreateForm
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
# from django.contrib.auth.mixins import rom django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, "bookings/home.html")


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


def clase_search_view(request):
    if request.method == "GET":
        form = ClaseSearchForm()
        return render(
            request, "bookings/form_search.html", context={"search_form": form}
        )
    elif request.method == "POST":
        form = ClaseSearchForm(request.POST)
        if form.is_valid():
            nombre_de_clase = form.cleaned_data["nombre"]
            clases_encontradas = Clase.objects.filter(nombre=nombre_de_clase).all()
            contexto_dict = {"todas_las_clases": clases_encontradas}
            return render(request, "bookings/vbc/clase_list.html", contexto_dict)
        else:
            return render(
                request, "bookings/form_search.html", context={"search_form": form}
            )
        

class GrupoListView(LoginRequiredMixin, ListView):
    model = Grupo
    template_name = "bookings/vbc/grupo_list.html"
    context_object_name = "todos_los_grupos"


class GrupoDetailView(LoginRequiredMixin, DetailView):
    model = Grupo
    template_name = "bookings/vbc/grupo_detail.html"
    context_object_name = "detalle_grupo"


class GrupoDeleteView(LoginRequiredMixin, DeleteView):
    model = Grupo
    template_name = "bookings/vbc/grupo_confirm_delete.html"
    success_url = reverse_lazy("grupo-list")


class GrupoUpdateView(LoginRequiredMixin, UpdateView):
    model = Grupo
    template_name = "bookings/vbc/grupo_form.html"
    fields = ["nombre", "size", "tipo", "descripcion"]
    context_object_name = "grupo"
    success_url = reverse_lazy("grupo-list")


class GrupoCreateView(LoginRequiredMixin, CreateView):
    model = Grupo
    template_name = "bookings/vbc/grupo_form.html"
    fields = ["nombre", "size", "tipo", "descripcion"]
    success_url = reverse_lazy("grupo-list")


def grupo_search_view(request):
    if request.method == "GET":
        form = GrupoSearchForm()
        return render(
            request, "bookings/form_search.html", context={"search_form": form}
        )
    elif request.method == "POST":
        form = GrupoSearchForm(request.POST)
        if form.is_valid():
            nombre_del_grupo = form.cleaned_data["nombre"]
            grupos_encontrados = Grupo.objects.filter(nombre=nombre_del_grupo).all()
            contexto_dict = {"todos_los_grupos": grupos_encontrados}
            return render(request, "bookings/vbc/grupo_list.html", contexto_dict)
        else:
            return render(
                request, "bookings/form_search.html", context={"search_form": form}
            )


class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = "bookings/vbc/reserva_list.html"
    context_object_name = "todas_las_reservas"


class ReservaDetailView(LoginRequiredMixin, DetailView):
    model = Reserva
    template_name = "bookings/vbc/reserva_detail.html"
    context_object_name = "reserva"


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = "bookings/vbc/reserva_confirm_delete.html"
    success_url = reverse_lazy("reserva-list")


class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    template_name = "bookings/vbc/reserva_form.html"
    fields = ["nombre", "clase","instrumento", "seccion", "experiencia", "presentacion", "fecha", "hora_inicio", "hora_fin"]
    context_object_name = "reserva"
    success_url = reverse_lazy("reserva-list")


class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = "bookings/vbc/reserva_form.html"
    fields = ["nombre", "clase","instrumento", "seccion", "experiencia", "presentacion", "fecha", "hora_inicio", "hora_fin"]
    success_url = reverse_lazy("reserva-list")


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "bookings/login.html", {"acceder": form})

def user_logout_view(request):
    logout(request)
    return redirect("login")

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'bookings/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    

def avatar_view(request):
    if request.method == "GET":
        contexto = {"avatar": AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user=request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user=request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"avatar": form}


    return render(request, "bookings/avatar_create.html", context=contexto)