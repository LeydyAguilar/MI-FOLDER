import tkinter as tk
import math
from typing import TypeVar, Generic

T = TypeVar("T", int, float)

# ---------- CLASES GENÉRICAS ----------
class FiguraGeometrica(Generic[T]):
    def area(self) -> T:
        raise NotImplementedError

    def perimetro(self) -> T:
        raise NotImplementedError


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


# ---------- DIBUJAR FIGURAS ----------
def dibujar_rectangulo(base, altura):
    canvas.delete("rect")  # SOLO borra los rectángulos

    escala = 5
    w = base * escala
    h = altura * escala

    x1, y1 = 80, 80
    x2, y2 = x1 + w, y1 + h

    rect = Rectangulo(base, altura)

    canvas.create_rectangle(
        x1, y1, x2, y2,
        fill="#64B5F6", outline="black", width=3, tag="rect"
    )

    texto = (
        f"Base: {base}\n"
        f"Altura: {altura}\n"
        f"Área: {rect.area():.2f}\n"
        f"Perímetro: {rect.perimetro():.2f}"
    )

    canvas.create_text(
        (x1 + x2) / 2,
        (y1 + y2) / 2,
        text=texto,
        font=("Comic Sans MS", 14, "bold"),
        fill="white",
        tag="rect"
    )


def dibujar_circulo(radio):
    canvas.delete("circ")  # SOLO borra los círculos

    escala = 5
    r = radio * escala

    cx = 1100
    cy = 180

    x1, y1 = cx - r, cy - r
    x2, y2 = cx + r, cy + r

    circ = Circulo(radio)

    canvas.create_oval(
        x1, y1, x2, y2,
        fill="#EF5350", outline="black", width=3, tag="circ"
    )

    texto = (
        f"Radio: {radio}\n"
        f"Área: {circ.area():.2f}\n"
        f"Perímetro: {circ.perimetro():.2f}"
    )

    canvas.create_text(
        cx,
        cy,
        text=texto,
        font=("Comic Sans MS", 14, "bold"),
        fill="white",
        tag="circ"
    )


# ---------- BORRAR TODO ----------
def borrar_todo():
    canvas.delete("all")
    resultado_rect.config(text="")
    resultado_circ.config(text="")


# ---------- CÁLCULOS ----------
def calcular_rectangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())

        rect = Rectangulo(base, altura)
        resultado_rect.config(
            text=f"Área: {rect.area():.2f} | Perímetro: {rect.perimetro():.2f}",
            fg="black"
        )

        dibujar_rectangulo(base, altura)

    except ValueError:
        resultado_rect.config(text="Valores inválidos", fg="red")


def calcular_circulo():
    try:
        radio = float(entry_radio.get())

        circ = Circulo(radio)
        resultado_circ.config(
            text=f"Área: {circ.area():.2f} | Perímetro: {circ.perimetro():.2f}",
            fg="black"
        )

        dibujar_circulo(radio)

    except ValueError:
        resultado_circ.config(text="Valor inválido", fg="red")


# ---------- INTERFAZ ----------
root = tk.Tk()
root.title("Figuras Geométricas a Color")

root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

root.config(bg="#FFF8E1")

titulo = tk.Label(
    root,
    text="🎨 Figuras Geométricas Dinámicas 🎨",
    font=("Comic Sans MS", 30, "bold"),
    bg="#FFF8E1",
    fg="#D84315"
)
titulo.pack(pady=20)

canvas = tk.Canvas(root, width=1400, height=400, bg="#FFECB3")
canvas.pack(pady=10)

# ----- BOTÓN BORRAR TODO -----
btn_clear = tk.Button(
    root,
    text="🗑 Borrar Todo",
    font=("Comic Sans MS", 18, "bold"),
    bg="#F4511E",
    fg="white",
    command=borrar_todo
)
btn_clear.pack(pady=10)


# ----- RECTÁNGULO -----
rect_frame = tk.Frame(root, bg="#FFF8E1")
rect_frame.pack(pady=20)

tk.Label(rect_frame, text="📘 Rectángulo Azul",
         font=("Comic Sans MS", 22, "bold"), bg="#FFF8E1").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(rect_frame, text="Base:", bg="#FFF8E1",
         font=("Comic Sans MS", 18)).grid(row=1, column=0)
entry_base = tk.Entry(rect_frame, font=("Comic Sans MS", 18))
entry_base.grid(row=1, column=1, padx=10)

tk.Label(rect_frame, text="Altura:", bg="#FFF8E1",
         font=("Comic Sans MS", 18)).grid(row=2, column=0)
entry_altura = tk.Entry(rect_frame, font=("Comic Sans MS", 18))
entry_altura.grid(row=2, column=1, padx=10)

btn_rect = tk.Button(rect_frame, text="Dibujar Rectángulo",
                     font=("Comic Sans MS", 18), bg="#64B5F6",
                     command=calcular_rectangulo)
btn_rect.grid(row=3, column=0, columnspan=2, pady=10)

resultado_rect = tk.Label(rect_frame, text="",
                          font=("Comic Sans MS", 18),
                          bg="#FFF8E1")
resultado_rect.grid(row=4, column=0, columnspan=2)


# ----- CÍRCULO -----
circ_frame = tk.Frame(root, bg="#FFF8E1")
circ_frame.pack(pady=20)

tk.Label(circ_frame, text="🔴 Círculo Rojo",
         font=("Comic Sans MS", 22, "bold"), bg="#FFF8E1").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(circ_frame, text="Radio:", bg="#FFF8E1",
         font=("Comic Sans MS", 18)).grid(row=1, column=0)
entry_radio = tk.Entry(circ_frame, font=("Comic Sans MS", 18))
entry_radio.grid(row=1, column=1, padx=10)

btn_circ = tk.Button(circ_frame, text="Dibujar Círculo",
                     font=("Comic Sans MS", 18), bg="#EF5350",
                     command=calcular_circulo)
btn_circ.grid(row=2, column=0, columnspan=2, pady=10)

resultado_circ = tk.Label(circ_frame, text="",
                          font=("Comic Sans MS", 18),
                          bg="#FFF8E1")
resultado_circ.grid(row=3, column=0, columnspan=2)

root.mainloop()




