import tkinter as tk

def fibonacci():
    lbl_error.config(text="", fg="red")
    lbl_resultado.config(text="")

    try:
        n = int(entry_n.get())

        if n <= 0:
            raise ValueError("El número debe ser positivo")

        # Generar e imprimir la serie sin listas
        a, b = 0, 1
        texto = ""

        for _ in range(n):
            texto += str(a) + ", "
            a, b = b, a + b

        texto = texto.rstrip(", ")  # ❗ quita la última coma

        lbl_resultado.config(text=texto, fg="#00FF7F")

    except ValueError as ve:
        lbl_error.config(text=str(ve))
        lbl_resultado.config(text="")

    except Exception as e:
        lbl_error.config(text="Error inesperado: " + str(e))
        lbl_resultado.config(text="")

def limpiar():
    entry_n.delete(0, tk.END)
    lbl_resultado.config(text="")
    lbl_error.config(text="")

# ---------------------------------------------------------
# INTERFAZ
# ---------------------------------------------------------

ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("500x350")
ventana.config(bg="#1E1E2E")  # Fondo oscuro moderno

# Título
titulo = tk.Label(ventana, text="Generador de Serie Fibonacci",
                  font=("Arial", 20, "bold"),
                  bg="#1E1E2E", fg="#89DCEB")
titulo.pack(pady=15)

# Entrada
frame_input = tk.Frame(ventana, bg="#1E1E2E")
frame_input.pack()

lbl_n = tk.Label(frame_input, text="Cantidad de términos:",
                 font=("Arial", 14),
                 bg="#1E1E2E", fg="white")
lbl_n.grid(row=0, column=0, padx=5, pady=5)

entry_n = tk.Entry(frame_input, font=("Arial", 14),
                   bg="#2A2A3C", fg="white", insertbackground="white")
entry_n.grid(row=0, column=1, padx=5, pady=5)

# Área de error
lbl_error = tk.Label(ventana, text="", font=("Arial", 12, "bold"),
                     bg="#1E1E2E", fg="red")
lbl_error.pack()

# Botones
frame_botones = tk.Frame(ventana, bg="#1E1E2E")
frame_botones.pack(pady=10)

btn_calc = tk.Button(frame_botones, text="Generar",
                     font=("Arial", 14, "bold"),
                     bg="#96CDFB", fg="black",
                     width=12, command=fibonacci)
btn_calc.grid(row=0, column=0, padx=10)

btn_limpiar = tk.Button(frame_botones, text="Limpiar",
                        font=("Arial", 14, "bold"),
                        bg="#F5C2E7", fg="black",
                        width=12, command=limpiar)
btn_limpiar.grid(row=0, column=1, padx=10)

# Resultado
lbl_resultado = tk.Label(ventana, text="",
                         font=("Arial", 14, "bold"),
                         bg="#1E1E2E", fg="white",
                         wraplength=450,
                         justify="left")
lbl_resultado.pack(pady=20)

ventana.mainloop()

