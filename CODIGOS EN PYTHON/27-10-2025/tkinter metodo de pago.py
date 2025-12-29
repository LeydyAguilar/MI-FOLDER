import tkinter as tk
from tkinter import ttk
from datetime import datetime

# === Clases base y derivadas ===
class MetodoDePago:
    def pagar(self, monto):
        pass


class TarjetaDeCredito(MetodoDePago):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular

    def pagar(self, monto):
        return f"💳 Pagando ${monto:.2f} con tarjeta de crédito a nombre de {self.titular}."


class PayPal(MetodoDePago):
    def __init__(self, correo):
        self.correo = correo

    def pagar(self, monto):
        return f"💻 Pagando ${monto:.2f} mediante PayPal con la cuenta {self.correo}."


class Efectivo(MetodoDePago):
    def pagar(self, monto):
        return f"💵 Pagando ${monto:.2f} en efectivo."


def procesar_pago(metodo, monto):
    return metodo.pagar(monto)


# === Ventana de inicio de sesión ===
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema - Boutique Fashion")
        self.root.geometry("380x260")
        self.root.config(bg="#F8EDEB")

        ttk.Style().configure("TButton", padding=6, relief="flat", background="#D8E2DC")
        ttk.Style().configure("TLabel", background="#F8EDEB")

        ttk.Label(root, text="👗 Boutique Fashion 👠", font=("Arial", 16, "bold"), background="#F8EDEB", foreground="#9D8189").pack(pady=10)
        ttk.Label(root, text="🔐 Inicio de Sesión", font=("Arial", 13, "bold"), background="#F8EDEB").pack(pady=5)

        ttk.Label(root, text="Usuario:").pack(pady=2)
        self.usuario_entry = ttk.Entry(root)
        self.usuario_entry.pack(pady=5)

        ttk.Label(root, text="Contraseña:").pack(pady=2)
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.mensaje_label = ttk.Label(root, text="", foreground="red", background="#F8EDEB")
        self.mensaje_label.pack(pady=5)

        ttk.Button(root, text="Ingresar", command=self.verificar_login).pack(pady=10)

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        password = self.password_entry.get()

        # Credenciales
        if usuario == "lady" and password == "2468":
            self.abrir_sistema_pagos()
        else:
            self.mensaje_label.config(text="❌ Usuario o contraseña incorrectos")

    def abrir_sistema_pagos(self):
        self.root.destroy()
        main_root = tk.Tk()
        app = App(main_root)
        main_root.mainloop()


# === Interfaz principal ===
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pagos - Boutique Fashion")
        self.root.geometry("450x560")
        self.root.config(padx=20, pady=20, bg="#F8EDEB")

        ttk.Style().configure("TButton", padding=6, relief="flat", background="#D8E2DC")
        ttk.Style().configure("TLabel", background="#F8EDEB")

        ttk.Label(root, text="💳 Sistema de Pagos", font=("Arial", 14, "bold"), foreground="#9D8189", background="#F8EDEB").pack(pady=10)
        ttk.Label(root, text="Seleccione un método de pago:", font=("Arial", 12), background="#F8EDEB").pack(pady=5)

        # Métodos de pago
        self.metodo_var = tk.StringVar()
        self.combo_metodo = ttk.Combobox(root, textvariable=self.metodo_var,
                                         values=["Tarjeta de crédito", "PayPal", "Efectivo"], state="readonly")
        self.combo_metodo.pack(pady=5)
        self.combo_metodo.bind("<<ComboboxSelected>>", self.mostrar_campos)

        # Frame dinámico
        self.frame_campos = ttk.Frame(root)
        self.frame_campos.pack(pady=10)

        # Monto
        ttk.Label(root, text="Monto a pagar:", background="#F8EDEB").pack()
        self.monto_entry = ttk.Entry(root)
        self.monto_entry.pack(pady=5)

        # Botones principales
        ttk.Button(root, text="Procesar pago", command=self.procesar).pack(pady=10)
        self.resultado_label = ttk.Label(root, text="", font=("Arial", 11, "bold"), background="#F8EDEB")
        self.resultado_label.pack(pady=10)

        self.btn_baucher = ttk.Button(root, text="🧾 Imprimir Baucher", command=self.imprimir_baucher, state="disabled")
        self.btn_baucher.pack(pady=10)

        # Botón de resumen del día
        ttk.Button(root, text="📊 Ver Resumen del Día", command=self.mostrar_resumen).pack(pady=10)

        # Variables
        self.ultimo_pago = None
        self.pagos_dia = []  # lista de todos los pagos del día

    def limpiar_campos(self):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()

    def mostrar_campos(self, event=None):
        self.limpiar_campos()
        metodo = self.metodo_var.get()

        if metodo == "Tarjeta de crédito":
            ttk.Label(self.frame_campos, text="Número de tarjeta:").grid(row=0, column=0)
            self.numero_entry = ttk.Entry(self.frame_campos)
            self.numero_entry.grid(row=0, column=1)
            ttk.Label(self.frame_campos, text="Titular:").grid(row=1, column=0)
            self.titular_entry = ttk.Entry(self.frame_campos)
            self.titular_entry.grid(row=1, column=1)

        elif metodo == "PayPal":
            ttk.Label(self.frame_campos, text="Correo de PayPal:").grid(row=0, column=0)
            self.correo_entry = ttk.Entry(self.frame_campos)
            self.correo_entry.grid(row=0, column=1)

        elif metodo == "Efectivo":
            ttk.Label(self.frame_campos, text="No se necesitan datos adicionales").grid(row=0, column=0)

    def procesar(self):
        metodo = self.metodo_var.get()
        monto_texto = self.monto_entry.get()

        try:
            monto = float(monto_texto)
        except ValueError:
            self.resultado_label.config(text="⚠️ Ingresa un monto válido.", foreground="red")
            return

        if metodo == "Tarjeta de crédito":
            numero = self.numero_entry.get()
            titular = self.titular_entry.get()
            if not numero or not titular:
                self.resultado_label.config(text="⚠️ Ingresa todos los datos.", foreground="red")
                return
            metodo_obj = TarjetaDeCredito(numero, titular)
            info = f"Titular: {titular}\nNúmero: {numero}"

        elif metodo == "PayPal":
            correo = self.correo_entry.get()
            if not correo:
                self.resultado_label.config(text="⚠️ Ingresa el correo de PayPal.", foreground="red")
                return
            metodo_obj = PayPal(correo)
            info = f"Cuenta: {correo}"

        elif metodo == "Efectivo":
            metodo_obj = Efectivo()
            info = "Pago en efectivo"

        else:
            self.resultado_label.config(text="⚠️ Selecciona un método de pago.", foreground="red")
            return

        resultado = procesar_pago(metodo_obj, monto)
        self.resultado_label.config(text=resultado, foreground="green")

        # Guardar pago
        pago = {
            "metodo": metodo,
            "info": info,
            "monto": monto,
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self.ultimo_pago = pago
        self.pagos_dia.append(pago)

        self.btn_baucher.config(state="normal")

    def imprimir_baucher(self):
        if not self.ultimo_pago:
            return

        ventana_baucher = tk.Toplevel(self.root)
        ventana_baucher.title("Baucher de Pago - Boutique Fashion")
        ventana_baucher.geometry("320x320")
        ventana_baucher.config(padx=20, pady=20, bg="white")

        ttk.Label(ventana_baucher, text="🧾 COMPROBANTE DE PAGO 🧾", font=("Arial", 12, "bold")).pack(pady=10)

        pago = self.ultimo_pago
        texto = (
            f"Tienda: Boutique Fashion\n\n"
            f"Método: {pago['metodo']}\n"
            f"{pago['info']}\n\n"
            f"Monto pagado: ${pago['monto']:.2f}\n"
            f"Fecha y hora: {pago['fecha']}\n\n"
            f"👗 ¡Gracias por su compra!"
        )

        tk.Label(ventana_baucher, text=texto, justify="left", bg="white", font=("Courier", 10)).pack(pady=10)
        ttk.Button(ventana_baucher, text="Cerrar", command=ventana_baucher.destroy).pack(pady=10)

    def mostrar_resumen(self):
        """Ventana emergente con el resumen de pagos del día"""
        if not self.pagos_dia:
            tk.messagebox.showinfo("Resumen del Día", "No se han registrado pagos hoy.")
            return

        ventana_resumen = tk.Toplevel(self.root)
        ventana_resumen.title("📊 Resumen del Día - Boutique Fashion")
        ventana_resumen.geometry("400x400")
        ventana_resumen.config(bg="#FFF", padx=20, pady=20)

        ttk.Label(ventana_resumen, text="📋 RESUMEN DE PAGOS DEL DÍA", font=("Arial", 12, "bold")).pack(pady=10)

        total_pagos = len(self.pagos_dia)
        total_monto = sum(p["monto"] for p in self.pagos_dia)

        ttk.Label(ventana_resumen, text=f"Total de pagos: {total_pagos}", font=("Arial", 11)).pack()
        ttk.Label(ventana_resumen, text=f"Total recaudado: ${total_monto:.2f}", font=("Arial", 11, "bold"), foreground="green").pack(pady=5)

        # Lista de pagos individuales
        texto = ""
        for i, pago in enumerate(self.pagos_dia, start=1):
            texto += f"{i}. {pago['metodo']} - ${pago['monto']:.2f}\n"

        text_box = tk.Text(ventana_resumen, width=45, height=12, wrap="word", bg="#FFF5F5")
        text_box.insert("1.0", texto)
        text_box.config(state="disabled")
        text_box.pack(pady=10)

        ttk.Button(ventana_resumen, text="Cerrar", command=ventana_resumen.destroy).pack(pady=10)


# === Ejecutar la app con Login ===
if __name__ == "__main__":
    root = tk.Tk()
    login = LoginWindow(root)
    root.mainloop()
