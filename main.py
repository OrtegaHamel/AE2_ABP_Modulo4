from tarjeta_credito import TarjetaCredito

# Creación de 3 tarjetas:

# Primera tarjeta: 2 compras y 1 pago
print("--- Información de la primera tarjeta ---")
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Segunda tarjeta: 3 compras y 2 pagos
print("\n--- Información de la segunda tarjeta ---")
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.05)
tarjeta2.compra(300).compra(400).compra(100).pago(150).pago(200).cobrar_interes().mostrar_info_tarjeta()

# Tercera tarjeta (intento de sobrepasar el límite)
print("\n--- Información de la tercera tarjeta ---")
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.03)
tarjeta3.compra(100).compra(150).compra(250).compra(150).compra(100).mostrar_info_tarjeta()

# BONUS: Mostrar todas las tarjetas creadas
print("\n--- Información de todas las tarjetas ---")
TarjetaCredito.mostrar_todas_las_tarjetas()