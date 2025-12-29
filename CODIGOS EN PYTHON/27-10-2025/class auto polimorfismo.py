class Vehiculo:
    def iniciar(self):
        print("El vehiculo esta listo para moverse")

class Coche(Vehiculo):
    def iniciar(self):
        print("Elcoche arranca y acelera")

class Bicicleta(Vehiculo):
    def iniciar(self):
        print("La bicicleta empieza a pedalear")

class Barco(Vehiculo):
    def iniciar(self):
        print("El barco enciende el motor y zarpa")

vehiculos = [Coche(),Bicicleta(),Barco()]

for v in vehiculos:
    v.iniciar()
