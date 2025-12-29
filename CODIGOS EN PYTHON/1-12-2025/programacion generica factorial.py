import tkinter as tk
from typing import TypeVar, Generic

T = TypeVar('T', int, float)

class CalculadoraFactorial(Generic[T]):
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def calcular():
    try:
        n = int(entry_numero.get())
        cal = CalculadoraFactorial(n)
        resultado = cal.calcular_factorial()

        label_resultado.config(
            text=f"Factorial de {n}: {resultado}",
            fg="white",
            bg="green"
        )

    except ValueError as e:
        label_resultado.config(
            text=f"Error: {str(e)}",
            fg="white",
            bg="red"
        )

def limpiar():
    entry_numero.delete(0, tk.END)
    label_resultado.config(text="", bg=ventana["bg"])

# --- INTERFAZ TKINTER ---
ventana = tk.Tk()
ventana.title("Calculadora de Factorial")
ventana.geometry("380x300")
ventana.config(bg="#1e1e2f")

# Título
label_titulo = tk.Label(
    ventana, 
    text="Calculadora de Factorial",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1e1e2f"
)
label_titulo.pack(pady=10)

# Ingreso
label_ingresar = tk.Label(
    ventana, 
    text="Ingrese un número:",
    font=("Arial", 12),
    fg="lightgray",
    bg="#1e1e2f"
)
label_ingresar.pack()

entry_numero = tk.Entry(
    ventana,
    font=("Arial", 12),
    justify="center",
    bg="#333344",
    fg="white",
    insertbackground="white"
)
entry_numero.pack(pady=5)

# Botón Calcular
btn_calcular = tk.Button(
    ventana,
    text="Calcular",
    font=("Arial", 12, "bold"),
    bg="#4b52d6",
    fg="white",
    activebackground="#6a6ff0",
    width=12,
    command=calcular
)
btn_calcular.pack(pady=8)

# Botón Limpiar
btn_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    font=("Arial", 12, "bold"),
    bg="#d64b4b",
    fg="white",
    activebackground="#f06a6a",
    width=12,
    command=limpiar
)
btn_limpiar.pack(pady=5)

# Resultado
label_resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f"
)
label_resultado.pack(pady=15)

ventana.mainloop()
