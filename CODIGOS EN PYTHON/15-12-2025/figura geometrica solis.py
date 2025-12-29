import math

# Principio S: Responsabilidad única
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("Las subclases deben implementar el método area")

    def perimetro(self):
        raise NotImplementedError("Las subclases deben implementar el método perimetro")


# Principios O y L
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Principio D
class Aplicacion:
    def __init__(self, figura):
        self.figura = figura

    def ejecutar(self):
        print(f"\nFigura: {self.figura.nombre}")
        print("Área:", self.figura.area())
        print("Perímetro:", self.figura.perimetro())

print("Seleccione la figura:")
print("1. Círculo")
print("2. Rectángulo")

opcion = input("Opción: ")

if opcion == "1":
    radio = float(input("Ingrese el radio del círculo: "))
    figura = Circulo(radio)

elif opcion == "2":
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    figura = Rectangulo(base, altura)

else:
    print("Opción no válida")
    exit()

# Ejecución
app = Aplicacion(figura)
app.ejecutar()

