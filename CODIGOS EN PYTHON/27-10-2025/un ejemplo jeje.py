class Circulo:
    def __init__(self,radio):
        self.radio = radio
    
    def area(self):
        print("El area del círculo es")
        return 3.141592 * (self.radio ** 2)

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
            
    def area(self):
        print("El area del rectangulo es")
        return self.base * self.altura

class Triangulo:
    def __init__(self,
    def area(self):
        print("El area del triangulo es")

def mostrar(figura):
    figura.dibujar()

figuras = [Circulo(), Rectangulo(), Triangulo()]

for figura in figuras:
    mostrar(figura)
