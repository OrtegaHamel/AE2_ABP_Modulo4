
# Simulador de Tarjetas de Crédito en Python
Por Álvaro Ortega Hamel

Este script en Python implementa una clase `TarjetaCredito` que permite simular el comportamiento básico de una tarjeta de crédito: compras, pagos, cobro de intereses y visualización del estado de cuenta. Además, mantiene un registro de todas las tarjetas creadas.

---

## Características

- Creación de tarjetas con límite de crédito e interés personalizado.
- Registro de compras y pagos.
- Control del saldo y validación del límite de crédito.
- Cálculo de intereses sobre el saldo actual.
- Visualización de la información individual de cada tarjeta.
- Visualización de todas las tarjetas creadas.

---

## Estructura del Código

### Clase `TarjetaCredito`

#### Atributos de instancia:
- `saldo_pagar`: Saldo acumulado por compras (por defecto 0).
- `limite_credito`: Límite máximo permitido para compras.
- `intereses`: Porcentaje de interés que se aplica al saldo.

#### Atributo de clase:
- `tarjetas_creadas`: Lista que almacena todas las tarjetas creadas.

#### Métodos:
- `compra(monto)`: Intenta realizar una compra. Si supera el límite, se rechaza.
- `pago(monto)`: Resta un monto al saldo pendiente.
- `cobrar_interes()`: Aplica intereses al saldo actual.
- `mostrar_info_tarjeta()`: Muestra la información actual de la tarjeta.
- `mostrar_todas_las_tarjetas()`: Método de clase que imprime la información de todas las tarjetas creadas.

---