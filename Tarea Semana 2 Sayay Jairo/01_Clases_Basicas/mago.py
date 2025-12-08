"""
CLASE: MAGO
Hereda de Personaje y añade atributo especial: LIBRO
"""

from personaje import Personaje

class Mago(Personaje):
    """Clase Mago - Especializado en daño mágico"""
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        """
        Inicializa un nuevo Mago
        
        Args:
            libro (int): Valor multiplicador de daño mágico del libro
        """
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        """Muestra los atributos del mago incluyendo su libro"""
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        """Calcula el daño: (Inteligencia × Libro) - Defensa del Enemigo"""
        return self.inteligencia * self.libro - enemigo.defensa
    
    def hechizo_especial(self, enemigo):
        """Hechizo que causa el doble de daño"""
        daño_especial = (self.inteligencia * self.libro) * 2 - enemigo.defensa
        enemigo.vida = enemigo.vida - daño_especial
        print(f"{self.nombre} lanza un HECHIZO ESPECIAL!")
        print(f"{self.nombre} ha realizado {daño_especial} puntos de daño a {enemigo.nombre}")
        
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre} es {enemigo.vida}")
        else:
            enemigo.morir()
