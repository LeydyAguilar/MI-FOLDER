from typing import TypeVar
import math

T = TypeVar('T', int, float)

def calcular_hipotenusa(cateto_a: T, cateto_b: T) -> T:
    return math.sqrt(cateto_a**2 + cateto_b**2)

def main():
    try:
        a = float(input("Ingrese el valor del cateto_a: "))
        b = float(input("Ingrese el valor del cateto_b: "))

        print("Hipotenusa =", calcular_hipotenusa(a, b))

    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

if __name__ == "__main__":
    main()
