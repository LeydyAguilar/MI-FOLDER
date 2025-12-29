import tkinter as tk
from typing import TypeVar, Generic

T = TypeVar("T", int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self) -> T:
        return self.a + self.b

    def restar(self) -> T:
        return self.a - self.b

    def multiplicar(self) -> T:
        return self.a * self.b

    def dividir(self) -> T:
        if self.b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return self.a / self.b

# ------------------- GUI -------------------

def operar(operacion):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        calc = Calculadora(a, b)

        if operacion == "sumar":
            resultado = calc.sumar()
        elif operacion == "restar":
            resultado = calc.restar()
        elif operacion == "multiplicar":
            resultado = calc.multiplicar()
        elif operacion == "dividir":
            resultado = calc.dividir()

        label_resultado.config(
            text=f"Resultado: {resultado}",
            fg="black"
        )

    except Exception as e:
        label_resultado.config(text=f"Error: {e}", fg="red")


# ------------------- DISEÑO INFANTIL -------------------

root = tk.Tk()
root.title("Calculadora para Niños")
root.geometry("500x380")
root.config(bg="#FCE4EC")   # rosa pastel suave

titulo = tk.Label(
    root,
    text="🧮 Calculadora Infantil 🧸",
    font=("Comic Sans MS", 22, "bold"),
    bg="#FCE4EC",
    fg="#D81B60"
)
titulo.pack(pady=10)

# Entradas con estilo infantil
frame_inputs = tk.Frame(root, bg="#FCE4EC")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Número A:", bg="#FCE4EC",
         font=("Comic Sans MS", 14)).grid(row=0, column=0, padx=10)
entry_a = tk.Entry(frame_inputs, font=("Comic Sans MS", 14), width=8, justify="center")
entry_a.grid(row=0, column=1)

tk.Label(frame_inputs, text="Número B:", bg="#FCE4EC",
         font=("Comic Sans MS", 14)).grid(row=1, column=0, padx=10)
entry_b = tk.Entry(frame_inputs, font=("Comic Sans MS", 14), width=8, justify="center")
entry_b.grid(row=1, column=1)

# Fila de botones grandes y coloridos
botones = tk.Frame(root, bg="#FCE4EC")
botones.pack(pady=20)

def boton(texto, color, oper):
    return tk.Button(
        botones,
        text=texto,
        font=("Comic Sans MS", 14, "bold"),
        width=10,
        height=2,
        bg=color,
        activebackground=color,
        command=lambda: operar(oper)
    )

boton("➕ Sumar", "#FFCDD2", "sumar").pack(side="left", padx=5)
boton("➖ Restar", "#F8BBD0", "restar").pack(side="left", padx=5)
boton("✖ Multiplicar", "#E1BEE7", "multiplicar").pack(side="left", padx=5)
boton("➗ Dividir", "#C5CAE9", "dividir").pack(side="left", padx=5)

# Área de resultado grande y visible
label_resultado = tk.Label(
    root,
    text="Resultado:",
    font=("Comic Sans MS", 18, "bold"),
    bg="#FCE4EC",
    fg="#880E4F"
)
label_resultado.pack(pady=15)

root.mainloop()

