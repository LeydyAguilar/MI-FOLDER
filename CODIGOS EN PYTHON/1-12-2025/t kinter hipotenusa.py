import tkinter as tk
import math

# ---------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------

def calcular():
    try:
        lbl_error.config(text="", fg="red")
        a = float(entry_a.get())
        b = float(entry_b.get())

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser positivos")

        hip = math.sqrt(a**2 + b**2)
        lbl_resultado.config(text=f"Hipotenusa: {hip:.2f}", fg="#00FF7F")

        dibujar_triangulo(a, b, hip)

    except ValueError as ve:
        lbl_error.config(text=str(ve))
        lbl_resultado.config(text="")
        canvas.delete("all")

    except Exception as e:
        lbl_error.config(text="Error inesperado: " + str(e))
        lbl_resultado.config(text="")
        canvas.delete("all")


def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    lbl_resultado.config(text="")
    lbl_error.config(text="")
    canvas.delete("all")


def dibujar_triangulo(a, b, hip):
    canvas.delete("all")

    escala = 200 / max(a, b)  
    ax, ay = 50, 250
    bx, by = ax + a * escala, ay
    cx, cy = ax, ay - b * escala

    # Triángulo
    canvas.create_polygon(
        ax, ay, bx, by, cx, cy,
        fill="#89DCEB", outline="white", width=3
    )

    # Etiquetas
    canvas.create_text((ax + bx) / 2, ay + 15, text=f"A={a}", fill="white", font=("Arial", 10, "bold"))
    canvas.create_text(ax - 30, (ay + cy) / 2, text=f"B={b}", fill="white", font=("Arial", 10, "bold"))
    canvas.create_text((bx + cx) / 2, (by + cy) / 2, text=f"H={hip:.2f}", fill="#00FF7F", font=("Arial", 10, "bold"))

# ---------------------------------------------------------
# INTERFAZ
# ---------------------------------------------------------

ventana = tk.Tk()
ventana.title("Calculadora de Hipotenusa PRO")
ventana.geometry("500x550")
ventana.config(bg="#1E1E2E")

# Esquinas redondeadas (simple frame simulando)
rounded = tk.Frame(ventana, bg="#1E1E2E", bd=0)
rounded.place(relwidth=1, relheight=1)

titulo = tk.Label(rounded, text="Calculadora de Hipotenusa",
                  font=("Arial", 20, "bold"), bg="#1E1E2E", fg="#89DCEB")
titulo.pack(pady=15)

frame_inputs = tk.Frame(rounded, bg="#1E1E2E")
frame_inputs.pack(pady=10)

lbl_a = tk.Label(frame_inputs, text="Cateto A:", font=("Arial", 14),
                 bg="#1E1E2E", fg="white")
lbl_a.grid(row=0, column=0, padx=5, pady=5)

entry_a = tk.Entry(frame_inputs, font=("Arial", 14), width=10, bg="#2A2A3C", fg="white", insertbackground="white")
entry_a.grid(row=0, column=1, padx=5, pady=5)

lbl_b = tk.Label(frame_inputs, text="Cateto B:", font=("Arial", 14),
                 bg="#1E1E2E", fg="white")
lbl_b.grid(row=1, column=0, padx=5, pady=5)

entry_b = tk.Entry(frame_inputs, font=("Arial", 14), width=10, bg="#2A2A3C", fg="white", insertbackground="white")
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Área de error
lbl_error = tk.Label(rounded, text="", font=("Arial", 12, "bold"), bg="#1E1E2E", fg="red")
lbl_error.pack()

# Botones
frame_botones = tk.Frame(rounded, bg="#1E1E2E")
frame_botones.pack(pady=10)

btn_calc = tk.Button(frame_botones, text="Calcular", font=("Arial", 14, "bold"),
                     bg="#96CDFB", fg="black", width=12, command=calcular)
btn_calc.grid(row=0, column=0, padx=10)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", font=("Arial", 14, "bold"),
                        bg="#F5C2E7", fg="black", width=12, command=limpiar)
btn_limpiar.grid(row=0, column=1, padx=10)

lbl_resultado = tk.Label(rounded, text="", font=("Arial", 16, "bold"),
                         bg="#1E1E2E", fg="white")
lbl_resultado.pack(pady=15)

# Canvas donde se dibuja el triángulo
canvas = tk.Canvas(rounded, width=400, height=300, bg="#2A2A3C", highlightthickness=0)
canvas.pack(pady=10)

ventana.mainloop()
