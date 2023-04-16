from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def crear_personaje(self):
        pass

    @abstractmethod
    def crear_enemigo(self):
        pass

class FactoryJugador(AbstractFactory):
    def crear_personaje(self):
        return Jugador()

    def crear_enemigo(self):
        return EnemigoFacil()

class FactoryEnemigo(AbstractFactory):
    def crear_personaje(self):
        return None

    def crear_enemigo(self):
        return EnemigoDificil()

class Jugador:
    def __init__(self):
        self.vida = 100
        self.ataque = 10

class EnemigoFacil:
    def __init__(self):
        self.vida = 50
        self.ataque = 5

class EnemigoDificil:
    def __init__(self):
        self.vida = 200
        self.ataque = 20

factory = FactoryJugador()
jugador = factory.crear_personaje()
enemigo = factory.crear_enemigo()
enemigo_dificil = FactoryEnemigo()
enemigo_dificil = enemigo_dificil.crear_enemigo()
