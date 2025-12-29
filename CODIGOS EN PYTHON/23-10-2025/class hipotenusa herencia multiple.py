import math

class Cateto_a:
    def __init__(self, cateto_a):
        self.cateto_a = cateto_a

class Cateto_b:
    def __init__(self, cateto_b):
        self.cateto_b = cateto_b

class Hipotenusa(Cateto_a, Cateto_b):
    def __init__(self, cateto_a, cateto_b):
        Cateto_a.__init__(self, cateto_a)
        Cateto_b.__init__(self, cateto_b)

    def calcular_hipotenusa(self):
        return math.sqrt(self.cateto_a**2 + self.cateto_b**2)

    def mostrar_resultado(self):
        h = self.calcular_hipotenusa()
        return f"Cateto a: {self.cateto_a}, Cateto b: {self.cateto_b} → Hipotenusa: {h:.2f}"


a = float(input("Ingrese el cateto a: "))
b = float(input("Ingrese el cateto b: "))

triangulo = Hipotenusa(a, b)
print(triangulo.mostrar_resultado())
