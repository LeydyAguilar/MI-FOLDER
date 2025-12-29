import tkinter as tk
from tkinter import ttk
import math

# === Clases de Figuras ===
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2


# === Interfaz Gráfica ===
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Áreas - Figuras Geométricas")
        self.root.geometry("400x500")
        self.root.config(padx=20, pady=20)

        # Selector de figura
        ttk.Label(root, text="Selecciona una figura:", font=("Arial", 12)).pack(pady=5)
        self.figura_var = tk.StringVar()
        self.combo_figura = ttk.Combobox(root, textvariable=self.figura_var,
                                         values=["Cuadrado", "Círculo", "Triángulo"], state="readonly")
        self.combo_figura.pack()
        self.combo_figura.bind("<<ComboboxSelected>>", self.mostrar_campos)

        # Frame para los campos de entrada
        self.frame_campos = ttk.Frame(root)
        self.frame_campos.pack(pady=10)

        # Botón para calcular
        self.btn_calcular = ttk.Button(root, text="Calcular Área", command=self.calcular_area)
        self.btn_calcular.pack(pady=10)

        # Resultado y mensajes
        self.mensaje_label = ttk.Label(root, text="", foreground="red", font=("Arial", 10))
        self.mensaje_label.pack()
        self.resultado_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
        self.resultado_label.pack(pady=10)

        # Canvas para dibujo
        self.canvas = tk.Canvas(root, width=200, height=200, bg="white", highlightthickness=1, relief="solid")
        self.canvas.pack(pady=10)

    def limpiar_campos(self):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()

    def mostrar_campos(self, event=None):
        self.limpiar_campos()
        self.mensaje_label.config(text="")
        figura = self.figura_var.get()

        if figura == "Cuadrado":
            ttk.Label(self.frame_campos, text="Lado:").grid(row=0, column=0)
            self.lado_entry = ttk.Entry(self.frame_campos)
            self.lado_entry.grid(row=0, column=1)
        elif figura == "Círculo":
            ttk.Label(self.frame_campos, text="Radio:").grid(row=0, column=0)
            self.radio_entry = ttk.Entry(self.frame_campos)
            self.radio_entry.grid(row=0, column=1)
        elif figura == "Triángulo":
            ttk.Label(self.frame_campos, text="Base:").grid(row=0, column=0)
            self.base_entry = ttk.Entry(self.frame_campos)
            self.base_entry.grid(row=0, column=1)
            ttk.Label(self.frame_campos, text="Altura:").grid(row=1, column=0)
            self.altura_entry = ttk.Entry(self.frame_campos)
            self.altura_entry.grid(row=1, column=1)

    def calcular_area(self):
        figura = self.figura_var.get()
        self.mensaje_label.config(text="")
        self.resultado_label.config(text="")
        self.canvas.delete("all")

        try:
            if figura == "Cuadrado":
                lado = float(self.lado_entry.get())
                figura_obj = Cuadrado(lado)
            elif figura == "Círculo":
                radio = float(self.radio_entry.get())
                figura_obj = Circulo(radio)
            elif figura == "Triángulo":
                base = float(self.base_entry.get())
                altura = float(self.altura_entry.get())
                figura_obj = Triangulo(base, altura)
            else:
                self.mensaje_label.config(text="⚠️ Selecciona una figura antes de continuar.")
                return

            area = figura_obj.area()
            self.resultado_label.config(text=f"Área: {area:.2f}")

            # === DIBUJO EN EL CANVAS ===
            if figura == "Cuadrado":
                self.canvas.create_rectangle(50, 50, 150, 150, fill="lightgreen", outline="green", width=2)

            elif figura == "Círculo":
                self.canvas.create_oval(50, 50, 150, 150, fill="lightblue", outline="blue", width=2)

            elif figura == "Triángulo":
                puntos = [100, 50, 50, 150, 150, 150]
                self.canvas.create_polygon(puntos, fill="lightcoral", outline="red", width=2)

        except ValueError:
            self.mensaje_label.config(text="⚠️ Ingresa valores numéricos válidos.")


# === Ejecutar la app ===
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

