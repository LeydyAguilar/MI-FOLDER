# producto
class Producto:
    def __init__(self, codigo, nombre, talla, estacion, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.talla = talla
        self.estacion = estacion
        self.precio = precio
        self.stock = 0

    def __str__(self):
        return (
            f"{self.codigo} | {self.nombre} | "
            f"Talla: {self.talla} | Estación: {self.estacion} | "
            f"Stock: {self.stock} | Precio: ${self.precio}"
        )
# producto.py

class Producto:
    def __init__(self, codigo, nombre, talla, estacion, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.talla = talla
        self.estacion = estacion
        self.precio = precio
        self.stock = 0

    def __str__(self):
        return (
            f"{self.codigo} | {self.nombre} | "
            f"Talla: {self.talla} | Estación: {self.estacion} | "
            f"Stock: {self.stock} | Precio: ${self.precio}"
        )
# sistema.py

class SistemaInventario:
    def __init__(self, inventario):
        self.inventario = inventario

    def mostrar_todo(self):
        print("\n--- INVENTARIO GENERAL ---")
        for producto in self.inventario.productos.values():
            print(producto)

    def mostrar_por_estacion(self, estacion):
        print(f"\n--- INVENTARIO {estacion.upper()} ---")
        encontrados = False
        for producto in self.inventario.productos.values():
            if producto.estacion.lower() == estacion.lower():
                print(producto)
                encontrados = True

        if not encontrados:
            print("No hay productos para esta estación")
# reportes.py

class ReporteInventario:
    def __init__(self, inventario):
        self.inventario = inventario

    def reporte_por_estacion(self, estacion):
        total = 0
        valor = 0

        for p in self.inventario.productos.values():
            if p.estacion.lower() == estacion.lower():
                total += p.stock
                valor += p.stock * p.precio

        print(f"\n--- REPORTE {estacion.upper()} ---")
        print(f"Total de prendas: {total}")
        print(f"Valor total: ${valor}")

    def reporte_general(self):
        total = sum(p.stock for p in self.inventario.productos.values())
        valor = sum(p.stock * p.precio for p in self.inventario.productos.values())

        print("\n--- REPORTE GENERAL ---")
        print(f"Total de prendas: {total}")
        print(f"Valor total del inventario: ${valor}")
# main.py

from producto import Producto
from inventario import Inventario
from sistema import SistemaInventario
from reportes import ReporteInventario

def main():
    inventario = Inventario()
    sistema = SistemaInventario(inventario)
    reporte = ReporteInventario(inventario)

    p1 = Producto("R001", "Camisa", "M", "Verano", 20)
    p2 = Producto("R002", "Abrigo", "L", "Invierno", 80)
    p3 = Producto("R003", "Chaqueta", "S", "Otoño", 60)

    inventario.registrar_producto(p1)
    inventario.registrar_producto(p2)
    inventario.registrar_producto(p3)

    inventario.entrada_stock("R001", 30)
    inventario.entrada_stock("R002", 15)
    inventario.entrada_stock("R003", 20)

    sistema.mostrar_todo()
    sistema.mostrar_por_estacion("Invierno")

    reporte.reporte_por_estacion("Invierno")
    reporte.reporte_general()

if __name__ == "__main__":
    main()

