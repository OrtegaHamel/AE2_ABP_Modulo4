class TarjetaCredito:
    tarjetas_creadas = [] # Lista de tarjetas creadas

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas_creadas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado el límite de crédito.")
        return self
    
    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
    
    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        print(f"Límite de crédito: ${self.limite_credito}")
        print(f"Interés: {self.intereses:.2f}%")
        return self
    
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self
    
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        for i, tarjeta in enumerate(cls.tarjetas_creadas, start=1):
            print(f"Tarjeta {i}:")
            tarjeta.mostrar_info_tarjeta()


# Creación de 3 tarjetas:

# Primera tarjeta: 2 compras y 1 pago
tarjeta1 = TarjetaCredito(limite_credito=1000, intereses=0.02)
tarjeta1.compra(200).compra(150).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Segunda tarjeta: 3 compras y 2 pagos
tarjeta2 = TarjetaCredito(limite_credito=2000, intereses=0.05)
tarjeta2.compra(300).compra(400).compra(100).pago(150).pago(200).cobrar_interes().mostrar_info_tarjeta()

# Tercera tarjeta (intento de sobrepasar el límite)
tarjeta3 = TarjetaCredito(limite_credito=500, intereses=0.03)
tarjeta3.compra(100).compra(150).compra(200).compra(50).compra(100).mostrar_info_tarjeta()

# BONUS: Mostrar todas las tarjetas creadas
print("\n--- Información de todas las tarjetas ---")
TarjetaCredito.mostrar_todas_las_tarjetas()