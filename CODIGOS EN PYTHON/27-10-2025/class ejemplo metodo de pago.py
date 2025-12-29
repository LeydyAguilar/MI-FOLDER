
class MetodoDePago:
    def pagar(self, monto):
        pass

class TarjetaDeCredito(MetodoDePago):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular

    def pagar(self, monto):
        print(f"Pagando ${monto:.2f} con tarjeta de crédito a nombre de {self.titular}.")


class PayPal(MetodoDePago):
    def __init__(self, correo):
        self.correo = correo

    def pagar(self, monto):
        print(f"Pagando ${monto:.2f} mediante PayPal con la cuenta {self.correo}.")


class Efectivo(MetodoDePago):
    def pagar(self, monto):
        print(f"Pagando ${monto:.2f} en efectivo.")

def procesar_pago(metodo, monto):
    metodo.pagar(monto)

pagos = [
    TarjetaDeCredito("1234-5678-9012-3456", "Juan Pérez"),
    PayPal("juanperez@email.com"),
    Efectivo()
]

for metodo in pagos:
    procesar_pago(metodo, 150.75)

    
