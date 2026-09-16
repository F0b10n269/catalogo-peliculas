from django.urls import path
from . import views

app_name = 'cartelera'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('pelicula/<int:id>/', views.detalle, name='detalle'),
]