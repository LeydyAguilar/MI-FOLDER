# Principio S
class Calculadora:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")


# Principios O y L
class Suma(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a + self.b


class Resta(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a - self.b


class Multiplicación(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a * self.b


class Division(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.b == 0:
            return "Error: división por cero"
        return self.a / self.b


# Principio D
class Aplicacion:
    def __init__(self, calculadora: Calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        print(f"Resultado: {self.calculadora.calcular()}")

print("CALCULADORA")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

print("\nSeleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Opción: ")

if opcion == "1":
    calculadora = Suma(a, b)
elif opcion == "2":
    calculadora = Resta(a, b)
elif opcion == "3":
    calculadora = Multiplicacion(a, b)
elif opcion == "4":
    calculadora = Division(a, b)
else:
    print("Opción inválida")
    exit()

app = Aplicacion(calculadora)
app.ejecutar()
