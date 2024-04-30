from django.urls import path

from .views import (
    home_view,
    ClaseListView,
    ClaseDetailView,
    ClaseDeleteView,
    ClaseUpdateView,
    ClaseCreateView,
    user_login_view,
    user_logout_view,
    UserUpdateView,
    clase_search_view,
)


urlpatterns = [
    path("", home_view, name="home"),
    path("clase/list/", ClaseListView.as_view(), name="clase-list"),
    path("clase/<int:pk>/detail/", ClaseDetailView.as_view(), name="clase-detail"),
    path("clase/<int:pk>/delete/", ClaseDeleteView.as_view(), name="clase-delete"),
    path("clase/<int:pk>/update/", ClaseUpdateView.as_view(), name="clase-update"),
    path("clase/create/", ClaseCreateView.as_view(), name="clase-create"),
    path("clase/buscar/", clase_search_view, name="clase-buscar"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),

]