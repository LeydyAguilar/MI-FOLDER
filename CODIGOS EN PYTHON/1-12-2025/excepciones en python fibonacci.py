import math

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    try:
        n = int(input("Ingrese cuántos términos desea de la serie de Fibonacci: "))

        if n <= 0:
            raise ValueError("El número debe ser positivo")

        print("Serie de Fibonacci:")
        fibonacci(n)

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()
