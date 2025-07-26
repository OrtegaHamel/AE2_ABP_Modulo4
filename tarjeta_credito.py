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
            print(f"No se pudo realizar la compra por {monto}. El total excede el límite de crédito.")
        return self
    
    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
    
    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: $ {self.saldo_pagar}")
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


