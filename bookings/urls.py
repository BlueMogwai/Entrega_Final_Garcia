from django.urls import path

from .views import (
    home_view,
    ClaseListView,
    ClaseDetailView,
    ClaseDeleteView,
    ClaseUpdateView,
    ClaseCreateView,
)


urlpatterns = [
    path("", home_view),
    path("clase/list/", ClaseListView.as_view(), name="clase-list"),
    path("clase/<int:pk>/detail/", ClaseDetailView.as_view(), name="clase-detail"),
    path("clase/<int:pk>/delete/", ClaseDeleteView.as_view(), name="clase-delete"),
    path("clase/<int:pk>/update/", ClaseUpdateView.as_view(), name="clase-update"),
    path("clase/create/", ClaseCreateView.as_view(), name="clase-create"),


]