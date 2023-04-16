from abc import ABC, abstractmethod

class PizzaFactory(ABC):
    @abstractmethod
    def crear_masa(self):
        pass

    @abstractmethod
    def crear_salsa(self):
        pass

    @abstractmethod
    def crear_toppings(self):
        pass

class PizzaHawaianaFactory(PizzaFactory):
    def crear_masa(self):
        return "Masa gruesa"

    def crear_salsa(self):
        return "Salsa de tomate"

    def crear_toppings(self):
        return ["Piña", "Jamón", "Queso"]

class PizzaPepperoniFactory(PizzaFactory):
    def crear_masa(self):
        return "Masa delgada"

    def crear_salsa(self):
        return "Salsa de tomate"

    def crear_toppings(self):
        return ["Pepperoni", "Queso"]

class Pizza:
    def __init__(self, masa, salsa, toppings):
        self.masa = masa
        self.salsa = salsa
        self.toppings = toppings

    def __str__(self):
        return f"Pizza de {self.masa} con {self.salsa} y toppings {', '.join(self.toppings)}"

factory_hawaiana = PizzaHawaianaFactory()
pizza_hawaiana = Pizza(factory_hawaiana.crear_masa(), factory_hawaiana.crear_salsa(), factory_hawaiana.crear_toppings())

factory_pepperoni = PizzaPepperoniFactory()
pizza_pepperoni = Pizza(factory_pepperoni.crear_masa(), factory_pepperoni.crear_salsa(), factory_pepperoni.crear_toppings())

print(pizza_hawaiana)
# Pizza de Masa gruesa con Salsa de tomate y toppings Piña, Jamón, Queso

print(pizza_pepperoni)
# Pizza de Masa delgada con Salsa de tomate y toppings Pepperoni, Queso
