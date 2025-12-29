import tkinter as tk

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return f"✅ El resultado de dividir {self.a} entre {self.b} es: {resultado}"
        except ZeroDivisionError:
            return "⚠️ Error: No se puede dividir entre cero. Intente con otro número."
        except Exception as e:
            # Mensaje más descriptivo
            return f"⚠️ Ocurrió un error inesperado durante la operación.\nDetalles técnicos: {e}"
        finally:
            print("Operación finalizada.")


def realizar_division():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        operacion = Division(a, b)
        resultado = operacion.dividir()
        label_resultado.config(text=resultado, fg="blue")

    except ValueError:
        label_resultado.config(
            text="⚠️ Error: Debe ingresar solo números (no letras ni símbolos).",
            fg="red"
        )


# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("División con Tkinter")
ventana.geometry("400x280")
ventana.resizable(False, False)
ventana.configure(bg="#f5f5f5")

# Título
titulo = tk.Label(
    ventana, 
    text="🧮 Calculadora de División", 
    font=("Arial", 14, "bold"), 
    bg="#f5f5f5"
)
titulo.pack(pady=10)

# Campo para el primer número
label_a = tk.Label(ventana, text="Ingrese el primer número:", bg="#f5f5f5")
label_a.pack()
entry_a = tk.Entry(ventana, font=("Arial", 11))
entry_a.pack(pady=5)

# Campo para el segundo número
label_b = tk.Label(ventana, text="Ingrese el segundo número:", bg="#f5f5f5")
label_b.pack()
entry_b = tk.Entry(ventana, font=("Arial", 11))
entry_b.pack(pady=5)

# Botón para dividir
boton_dividir = tk.Button(
    ventana, 
    text="Dividir", 
    command=realizar_division, 
    bg="#4CAF50", 
    fg="white", 
    font=("Arial", 11, "bold"), 
    width=12
)
boton_dividir.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(
    ventana, 
    text="", 
    font=("Arial", 12), 
    bg="#f5f5f5", 
    wraplength=350,  # para que el texto largo se divida en líneas
    justify="center"
)
label_resultado.pack(pady=15)

# Iniciar ventana
ventana.mainloop()



        
            
