class Animal:  # clase base
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hacerSonido(self):
        pass

class Perro(Animal):  # clase derivada
    def hacerSonido(self):
        return "¡Guau!"

class Gato(Animal):  # clase derivada
    def hacerSonido(self):
        return "¡Miau!"
        
perro = Perro("Rex")
print(f"{perro.nombre} dice {perro.hacerSonido()}")

gato = Gato("Pelusa")
print(f"{gato.nombre} dice {gato.hacerSonido()}")
