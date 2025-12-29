# Principio S: Responsabilidad única
class Calculadora:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")


# Principios O y L
class Factorial(Calculadora):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        resultado = 1
        for i in range(1, self.numero + 1):
            resultado *= i
        return resultado


class TrianguloRectangulo(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        hipotenusa = (self.a ** 2 + self.b ** 2) ** 0.5
        return hipotenusa

class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print("Resultado:", resultado)

triangulo = TrianguloRectangulo(3, 4)
app2 = Aplicacion(triangulo)
app2.ejecutar()
