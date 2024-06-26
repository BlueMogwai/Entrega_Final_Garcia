from django.urls import path

from .views import (
    home_view,
    about_view,
    ClaseListView,
    ClaseDetailView,
    ClaseDeleteView,
    ClaseUpdateView,
    ClaseCreateView,
    user_creation_view,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    clase_search_view,
    GrupoListView,
    GrupoDetailView,
    GrupoDeleteView,
    GrupoUpdateView,
    GrupoCreateView,
    grupo_search_view,
    ReservaListView,
    ReservaDetailView,
    ReservaDeleteView,
    ReservaUpdateView,
    ReservaCreateView,
    avatar_view,

)


urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("clase/list/", ClaseListView.as_view(), name="clase-list"),
    path("clase/<int:pk>/detail/", ClaseDetailView.as_view(), name="clase-detail"),
    path("clase/<int:pk>/delete/", ClaseDeleteView.as_view(), name="clase-delete"),
    path("clase/<int:pk>/update/", ClaseUpdateView.as_view(), name="clase-update"),
    path("clase/create/", ClaseCreateView.as_view(), name="clase-create"),
    path("clase/buscar/", clase_search_view, name="clase-buscar"),
    path("grupo/list/", GrupoListView.as_view(), name="grupo-list"),
    path("grupo/<int:pk>/detail/", GrupoDetailView.as_view(), name="grupo-detail"),
    path("grupo/<int:pk>/delete/", GrupoDeleteView.as_view(), name="grupo-delete"),
    path("grupo/<int:pk>/update/", GrupoUpdateView.as_view(), name="grupo-update"),
    path("grupo/create/", GrupoCreateView.as_view(), name="grupo-create"),
    path("reserva/buscar/", grupo_search_view, name="grupo-buscar"),
    path("reserva/list/", ReservaListView.as_view(), name="reserva-list"),
    path("reserva/<int:pk>/detail/", ReservaDetailView.as_view(), name="reserva-detail"),
    path("reserva/<int:pk>/delete/", ReservaDeleteView.as_view(), name="reserva-delete"),
    path("reserva/<int:pk>/update/", ReservaUpdateView.as_view(), name="reserva-update"),
    path("reserva/create/", ReservaCreateView.as_view(), name="reserva-create"),
    path("crear-usuario/", user_creation_view, name='crear-usuario'),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    path('avatar/add/',avatar_view, name='avatar_add'),

]