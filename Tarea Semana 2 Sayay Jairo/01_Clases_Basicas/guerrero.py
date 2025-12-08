"""
CLASE: GUERRERO
Hereda de Personaje y añade atributo especial: ESPADA
"""

from personaje import Personaje

class Guerrero(Personaje):
    """Clase Guerrero - Especializado en daño físico"""
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        """
        Inicializa un nuevo Guerrero
        
        Args:
            espada (int): Valor multiplicador de daño de la espada
        """
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        """Permite al guerrero cambiar su arma"""
        print("\n=== CAMBIAR ARMA ===")
        print("(1) Acero Valyrio - Daño 8")
        print("(2) Matadragones - Daño 10")
        print("(3) Excalibur - Daño 15")
        
        opcion = int(input("Elige un arma: "))
        
        if opcion == 1:
            self.espada = 8
            print(f"Ahora usas Acero Valyrio")
        elif opcion == 2:
            self.espada = 10
            print(f"Ahora usas Matadragones")
        elif opcion == 3:
            self.espada = 15
            print(f"Ahora usas Excalibur")
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        """Muestra los atributos del guerrero incluyendo su espada"""
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        """Calcula el daño: (Fuerza × Espada) - Defensa del Enemigo"""
        return self.fuerza * self.espada - enemigo.defensa
