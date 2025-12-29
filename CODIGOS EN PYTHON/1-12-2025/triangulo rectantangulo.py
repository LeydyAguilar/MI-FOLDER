from typing import TypeVar,Generic
import math
T = TypeVar('T',int,float)

class TrianguloRectangulo(Generic[T]):
    def __init__(self,a:T,b:T):
        self.a = a
        self.b = b

def calcular_hipotenusa(self)->int:
    return math.sqrt(self.a**2 + self.b**2)
    
def calcular_Area(self)->int:
    return(self.a* self.b)/2
    
def calcular_perimetro(self)->int:
    return self.a + self.b + self.calcular_hipotenusa()

def main() :
    try:
        a = int(input("Ingrese el cateto a: "))
        b = int(input("Ingrese el cateto b: "))

        tri = TrianguloRectangulo(a,b)

        print(f"Hipotenusa: {tri.calcular_hipotenusa():2f}")
        print(f"Area: {tri.calcular_Area():2f}")
        print(f"perimetro: {tri.calcular_perimetro():2f}")

     except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()


     
    
