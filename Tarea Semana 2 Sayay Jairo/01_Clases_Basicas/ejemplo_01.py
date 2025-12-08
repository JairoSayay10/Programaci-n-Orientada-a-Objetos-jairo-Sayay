"""
EJEMPLO 1: USO BÁSICO DE CLASES Y HERENCIA
Demuestra la creación de personajes y sus atributos
"""

from guerrero import Guerrero
from mago import Mago

def main():
    print("="*50)
    print("EJEMPLO 1: CREAR Y MOSTRAR PERSONAJES")
    print("="*50)
    
    # Crear un Guerrero
    guts = Guerrero("Guts", 20, 10, 4, 100, 4)
    
    # Crear un Mago
    vanessa = Mago("Vanessa", 5, 15, 4, 100, 3)
    
    # Mostrar atributos
    print("\n--- ATRIBUTOS INICIALES ---")
    guts.atributos()
    print()
    vanessa.atributos()
    
    # Subir nivel
    print("\n--- SUBIR NIVEL ---")
    guts.subir_nivel(5, 3, 2)
    vanessa.subir_nivel(2, 5, 1)
    
    print("\n--- ATRIBUTOS DESPUÉS DE SUBIR NIVEL ---")
    guts.atributos()
    print()
    vanessa.atributos()
    
    # Cambiar arma
    print("\n--- CAMBIAR ARMA ---")
    guts.cambiar_arma()
    guts.atributos()

if __name__ == "__main__":
    main()
