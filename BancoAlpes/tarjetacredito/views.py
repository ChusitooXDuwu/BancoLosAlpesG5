from django.shortcuts import render, get_object_or_404
from .models import Cliente, TarjetaCredito

def lista_tarjetas(request):
    tarjetas = TarjetaCredito.objects.all()
    return render(request, 'lista_tarjetas.html', {'tarjetas': tarjetas})

def detalle_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(TarjetaCredito, id=tarjeta_id)
    return render(request, 'detalle_tarjeta.html', {'tarjeta': tarjeta})

