from typing import TypeVar, Generic
T = TypeVar("T", int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        try:
            self.a = a
            self.b = b
        except Exception as e:
            raise TypeError(f"Error al asignar valores: {e}")

    def sumar(self) -> T:
        try:
            return self.a + self.b
        except Exception as e:
            raise TypeError(f"Error al sumar: {e}")

    def restar(self) -> T:
        try:
            return self.a - self.b
        except Exception as e:
            raise TypeError(f"Error al restar: {e}")

    def multiplicar(self) -> T:
        try:
            return self.a * self.b
        except Exception as e:
            raise TypeError(f"Error al multiplicar: {e}")

    def dividir(self) -> T:
        try:
            if self.b == 0:
                raise ZeroDivisionError("No se puede dividir entre cero")
            return self.a / self.b
        except Exception as e:
            raise ArithmeticError(f"Error al dividir: {e}")
def main():
    try:
        cal_int = Calculadora[int](a,5)
        print("Suma:", cal_int.sumar())
        print("Resta: ",cal_int.restar())
        print("Multiplicar: ",cal_int.multiplicar())
        print("Dividir: ",cal_int.dividir())

        cal_float = Calculadora[float](10.5, 2.5)
        print("Suma:", cal_float.sumar())
        print("Resta:", cal_float.restar())
        print("Multiplicar:", cal_float.multiplicar())
        print("Dividir:", cal_float.dividir())
    except Exception as error:
        print(f"Ocurrio un error: {error}")
if __name__=="__main__":
    main()
