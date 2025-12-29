import tkinter as tk
from tkinter import ttk, messagebox

# ========== CLASES BASE ==========
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        return f"Trabajo como {self.profesion} y gano ${self.salario:.2f} al mes."


class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"Estudio {self.carrera} en la universidad {self.universidad}."


# ========== CLASE MULTIROL ==========
class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        return (
            f"{self.presentarse()}\n"
            f"{self.trabajar()}\n"
            f"{self.estudiar()}\n"
        )


# ========== INTERFAZ GRÁFICA ==========
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Personas Multirol")
        self.root.geometry("700x750")
        self.root.configure(bg="#D7E9F7")

        # Título
        titulo = tk.Label(
            self.root, text="REGISTRO DE TRES PERSONAS", 
            font=("Arial", 16, "bold"), bg="#274472", fg="white", pady=10
        )
        titulo.pack(fill="x", pady=(0, 10))

        self.personas = []
        self.crear_formularios()

        # Botón principal
        boton = tk.Button(
            self.root, text="MOSTRAR INFORMACIÓN",
            font=("Arial", 11, "bold"), bg="#0096FF", fg="white",
            command=self.mostrar_todo
        )
        boton.pack(pady=15)

        # Cuadro de texto
        self.texto_resultado = tk.Text(
            self.root, height=12, wrap="word", bg="#F8F9FA",
            font=("Consolas", 10), state="normal"
        )
        self.texto_resultado.pack(padx=15, pady=10, fill="both")

    def crear_formularios(self):
        colores = ["#A8D8EA", "#AAE3E2", "#F9D5E5"]
        self.entradas = []

        for i in range(3):
            frame = tk.LabelFrame(
                self.root, text=f"Persona {i+1}",
                bg=colores[i], font=("Arial", 11, "bold"), padx=10, pady=10
            )
            frame.pack(fill="x", padx=15, pady=5)

            campos = {}
            etiquetas = [
                ("Nombre:", "nombre"),
                ("Edad:", "edad"),
                ("Profesión:", "profesion"),
                ("Salario:", "salario"),
                ("Carrera:", "carrera"),
                ("Universidad:", "universidad"),
            ]

            for texto, clave in etiquetas:
                tk.Label(frame, text=texto, bg=colores[i], font=("Arial", 10)).pack(anchor="w")
                entrada = ttk.Entry(frame)
                entrada.pack(fill="x", pady=3)
                campos[clave] = entrada

            self.entradas.append(campos)

    def mostrar_todo(self):
        resultados = ""
        self.texto_resultado.config(state="normal")
        self.texto_resultado.delete("1.0", tk.END)

        try:
            for i, campos in enumerate(self.entradas):
                nombre = campos["nombre"].get().strip()
                edad_texto = campos["edad"].get().strip()
                profesion = campos["profesion"].get().strip()
                salario_texto = campos["salario"].get().strip()
                carrera = campos["carrera"].get().strip()
                universidad = campos["universidad"].get().strip()

                # Validación básica
                if not nombre or not edad_texto or not profesion or not salario_texto or not carrera or not universidad:
                    messagebox.showwarning("Campos vacíos", f"Por favor complete todos los datos de la persona {i+1}.")
                    return

                edad = int(edad_texto)
                salario = float(salario_texto)

                persona = PersonaMultirol(nombre, edad, profesion, salario, carrera, universidad)
                resultados += f"===== PERSONA {i+1} =====\n{persona.mostrar_informacion()}\n"

            # Mostrar resultados
            self.texto_resultado.insert(tk.END, resultados)
            self.texto_resultado.config(state="disabled")

        except ValueError:
            messagebox.showerror("Error", "Edad y salario deben ser números válidos.")
            self.texto_resultado.config(state="disabled")


# ========== EJECUCIÓN ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
