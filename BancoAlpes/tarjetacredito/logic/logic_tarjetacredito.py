from ..models import Cliente, TarjetaCredito

def crear_tarjeta_credito(cliente_id, tipo, activa, cupo):
    cliente = Cliente.objects.get(id=cliente_id)
    tarjeta = TarjetaCredito.objects.create(cliente=cliente, tipo=tipo, activa=activa, cupo=cupo)
    return tarjeta

def obtener_tarjeta_credito(id):
    return TarjetaCredito.objects.get(id=id)

def obtener_tarjetas_credito():
    return TarjetaCredito.objects.all()

def actualizar_tarjeta_credito(id, tipo, activa, cupo):
    tarjeta = TarjetaCredito.objects.get(id=id)
    tarjeta.tipo = tipo
    tarjeta.activa = activa
    tarjeta.cupo = cupo
    tarjeta.save()
    return tarjeta

def eliminar_tarjeta_credito(id):
    tarjeta = TarjetaCredito.objects.get(id=id)
    tarjeta.delete()
    return tarjeta

def obtener_tarjetas_credito_cliente(cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return TarjetaCredito.objects.filter(cliente=cliente)