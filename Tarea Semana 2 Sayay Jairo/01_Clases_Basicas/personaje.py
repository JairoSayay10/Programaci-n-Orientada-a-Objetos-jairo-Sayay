"""
CLASE BASE: PERSONAJE
Contiene los atributos y métodos base para todos los personajes
"""

class Personaje:
    """Clase base para todos los personajes del juego"""
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        """
        Inicializa un nuevo personaje
        
        Args:
            nombre (str): Nombre del personaje
            fuerza (int): Valor de fuerza
            inteligencia (int): Valor de inteligencia
            defensa (int): Valor de defensa
            vida (int): Puntos de vida
        """
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        """Muestra los atributos del personaje"""
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        """Aumenta los atributos del personaje"""
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        print(f"{self.nombre} ha subido de nivel!")

    def esta_vivo(self):
        """Retorna True si el personaje está vivo"""
        return self.vida > 0

    def morir(self):
        """Mata al personaje"""
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        """Calcula el daño causado a un enemigo"""
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        """Realiza un ataque a un enemigo"""
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
