from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('tarjetas/', views.lista_tarjetas, name='lista_tarjetas'),
    path('tarjetas/<int:tarjeta_id>/', views.detalle_tarjeta, name='detalle_tarjeta'),
]
