from typing import TypeVar, Generic
import math
T = TypeVar("T", int, float)

class FiguraGeometrica(Generic[T]):
    def area(self) -> T:
        raise NotImplementedError("El método área debe ser implementado en la subclase.")

    def perimetro(self) -> T:
        raise NotImplementedError("El método perímetro debe ser implementado en la subclase.")

class Rectangulo(FiguraGeometrica[T]):
    def __init__(self, base: T, altura: T):
        self.base = base
        self.altura = altura

    def area(self) -> T:
        return self.base * self.altura

    def perimetro(self) -> T:
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica[T]):
    def __init__(self, radio: T):
        self.radio = radio

    def area(self) -> T:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> T:
        return 2 * math.pi * self.radio


if __name__ == "__main__":
    rect = Rectangulo(5, 3)
    print("Rectángulo:")
    print("Área:", rect.area())
    print("Perímetro:", rect.perimetro())

    circ = Circulo(4)
    print("\nCírculo:")
    print("Área:", circ.area())
    print("Perímetro:", circ.perimetro())
