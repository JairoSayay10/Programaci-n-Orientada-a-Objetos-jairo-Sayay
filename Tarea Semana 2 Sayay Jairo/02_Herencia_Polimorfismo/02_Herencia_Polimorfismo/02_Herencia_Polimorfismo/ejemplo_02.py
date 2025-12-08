"""
EJEMPLO 2: COMBATE COMPLETO CON POLIMORFISMO
Demuestra cómo diferentes clases calculan daño diferente
"""

import sys
sys.path.append('../01_Clases_Basicas')

from guerrero import Guerrero
from mago import Mago
from sistema_combate import combate, combate_con_estadisticas

def main():
    print("="*70)
    print("EJEMPLO 2: COMBATE CON POLIMORFISMO")
    print("="*70)
    
    # Crear personajes
    print("\n--- CREANDO PERSONAJES ---")
    guts = Guerrero("Guts", 20, 10, 4, 100, 4)
    vanessa = Mago("Vanessa", 5, 15, 4, 100, 3)
    
    print("\n--- ATRIBUTOS DE LOS PERSONAJES ---")
    guts.atributos()
    print()
    vanessa.atributos()
    
    # Demostrar cálculo de daño (polimorfismo)
    print("\n--- DEMOSTRACIÓN DE POLIMORFISMO (CÁLCULO DE DAÑO) ---")
    daño_guts = guts.daño(vanessa)
    daño_vanessa = vanessa.daño(guts)
    
    print(f"\nDaño de Guts a Vanessa: {daño_guts}")
    print(f"  Fórmula Guerrero: (Fuerza × Espada) - Defensa Enemigo")
    print(f"  Cálculo: (20 × 4) - 4 = {daño_guts}")
    
    print(f"\nDaño de Vanessa a Guts: {daño_vanessa}")
    print(f"  Fórmula Mago: (Inteligencia × Libro) - Defensa Enemigo")
    print(f"  Cálculo: (15 × 3) - 4 = {daño_vanessa}")
    
    # Iniciar combate
    print("\n" + "="*70)
    print("INICIANDO COMBATE")
    print("="*70)
    
    # Crear nuevos personajes para el combate
    guts2 = Guerrero("Guts", 20, 10, 4, 100, 4)
    vanessa2 = Mago("Vanessa", 5, 15, 4, 100, 3)
    
    combate_con_estadisticas(guts2, vanessa2)

if __name__ == "__main__":
    main()
