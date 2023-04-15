from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

class FabricaAnimales:
    def crear_animal(self, tipo):
        if tipo == 'perro':
            return Perro()
        elif tipo == 'gato':
            return Gato()
        else:
            raise ValueError("Tipo de animal no válido")
        
fabrica = FabricaAnimales()

animal1 = fabrica.crear_animal('perro')
print(animal1.hablar())  # Output: Guau!

animal2 = fabrica.crear_animal('gato')
print(animal2.hablar())  # Output: Miau!
