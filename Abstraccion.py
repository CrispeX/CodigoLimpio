from abc import ABC, abstractmethod
from typing import final

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float): ...

    @final
    def mensaje_final(self):
        print("gracias por su compra")

class TarjetaCredito(MetodoPago):
    def __init__(self, numero_tarjeta:str, cvv:str) -> None:
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv
    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} con tarjeta de crédito")

class PayPal(MetodoPago):
    def __init__(self, correo) -> None:
        self.correo = correo
    def procesar_pago(self, monto):
        print(f"Procesando pago de {monto} con PayPal")

pago_tarjeta = TarjetaCredito("123200988", "450")
pago_paypal = PayPal("usuario@paypal.com")

pago_tarjeta.procesar_pago(100)

pago_paypal.mensaje_final()
pago_tarjeta.mensaje_final()