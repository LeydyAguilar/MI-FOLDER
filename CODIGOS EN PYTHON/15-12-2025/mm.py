import math
import tkinter as tk

# ===============================
# LÓGICA (SOLID)
# ===============================

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Aplicacion:
    def __init__(self, figura):
        self.figura = figura

    def ejecutar(self):
        return self.figura.area(), self.figura.perimetro()


# ===============================
# INTERFAZ + GRÁFICO
# ===============================

def calcular():
    canvas.delete("all")

    try:
        if opcion.get() == "Circulo":
            radio = float(entry_radio.get())
            figura = Circulo(radio)

            # Escala para que quepa
            r = min(radio * 5, 80)
            x, y = 100, 100
            canvas.create_oval(
                x - r, y - r, x + r, y + r,
                outline="white", width=3
            )

        else:
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            figura = Rectangulo(base, altura)

            # Escala
            b = min(base * 5, 160)
            h = min(altura * 5, 100)
            canvas.create_rectangle(
                20, 20, 20 + b, 20 + h,
                outline="white", width=3
            )

        app = Aplicacion(figura)
        area, perimetro = app.ejecutar()

        resultado_label.config(
            text=f"Figura: {figura.nombre}\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}",
            bg="#2ecc71",
            fg="white"
        )

    except ValueError:
        resultado_label.config(
            text="Error: ingrese valores numéricos",
            bg="#e74c3c",
            fg="white"
        )


def cambiar_figura(*args):
    canvas.delete("all")
    if opcion.get() == "Circulo":
        frame_circulo.pack()
        frame_rectangulo.pack_forget()
    else:
        frame_rectangulo.pack()
        frame_circulo.pack_forget()


# ===============================
# VENTANA
# ===============================

root = tk.Tk()
root.title("Figuras Geométricas")
root.geometry("420x450")
root.config(bg="#34495e")

opcion = tk.StringVar(value="Circulo")
opcion.trace("w", cambiar_figura)

tk.Label(root, text="Seleccione la figura", bg="#34495e",
         fg="white", font=("Arial", 12, "bold")).pack()

tk.Radiobutton(root, text="Círculo", variable=opcion, value="Circulo",
               bg="#34495e", fg="white", selectcolor="#34495e").pack()

tk.Radiobutton(root, text="Rectángulo", variable=opcion, value="Rectangulo",
               bg="#34495e", fg="white", selectcolor="#34495e").pack()

# Entradas
frame_circulo = tk.Frame(root, bg="#34495e")
tk.Label(frame_circulo, text="Radio:", bg="#34495e", fg="white").pack()
entry_radio = tk.Entry(frame_circulo)
entry_radio.pack()

frame_rectangulo = tk.Frame(root, bg="#34495e")
tk.Label(frame_rectangulo, text="Base:", bg="#34495e", fg="white").pack()
entry_base = tk.Entry(frame_rectangulo)
entry_base.pack()

tk.Label(frame_rectangulo, text="Altura:", bg="#34495e", fg="white").pack()
entry_altura = tk.Entry(frame_rectangulo)
entry_altura.pack()

frame_circulo.pack()

# Canvas (dibujo)
canvas = tk.Canvas(root, width=200, height=200, bg="#2c3e50", highlightthickness=0)
canvas.pack(pady=10)

# Botón
tk.Button(root, text="Calcular", command=calcular,
          bg="#3498db", fg="white",
          font=("Arial", 11, "bold")).pack(pady=10)

# Resultado
resultado_label = tk.Label(root, bg="#34495e", fg="white",
                           font=("Arial", 11), width=30, height=4)
resultado_label.pack()

root.mainloop()
