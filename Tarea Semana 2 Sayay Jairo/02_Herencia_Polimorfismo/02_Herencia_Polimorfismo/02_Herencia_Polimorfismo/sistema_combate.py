"""
SISTEMA DE COMBATE
Implementa la lógica del combate por turnos
"""

import sys
sys.path.append('../01_Clases_Basicas')

from guerrero import Guerrero
from mago import Mago

def combate(jugador_1, jugador_2):
    """
    Simula un combate por turnos entre dos personajes
    
    Args:
        jugador_1: Primer personaje
        jugador_2: Segundo personaje
    """
    turno = 1
    
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n{'='*50} Turno {turno} {'='*50}")
        
        print(f"\n>>> Acción de {jugador_1.nombre}:")
        jugador_1.atacar(jugador_2)
        
        if not jugador_2.esta_vivo():
            break
        
        print(f"\n>>> Acción de {jugador_2.nombre}:")
        jugador_2.atacar(jugador_1)
        
        turno = turno + 1

    print(f"\n{'='*60} FIN DEL COMBATE {'='*60}")
    
    if jugador_1.esta_vivo():
        print(f"🏆 ¡HA GANADO: {jugador_1.nombre}!")
    elif jugador_2.esta_vivo():
        print(f"🏆 ¡HA GANADO: {jugador_2.nombre}!")
    else:
        print("⚖️  EMPATE - Ambos personajes han muerto")

def combate_con_estadisticas(jugador_1, jugador_2):
    """Combate que muestra estadísticas detalladas"""
    turno = 1
    daño_total_j1 = 0
    daño_total_j2 = 0
    
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n{'='*50} Turno {turno} {'='*50}")
        
        # Turno jugador 1
        print(f"\n>>> Acción de {jugador_1.nombre}:")
        vida_anterior_j2 = jugador_2.vida
        jugador_1.atacar(jugador_2)
        daño = vida_anterior_j2 - jugador_2.vida
        daño_total_j1 += daño
        
        if not jugador_2.esta_vivo():
            break
        
        # Turno jugador 2
        print(f"\n>>> Acción de {jugador_2.nombre}:")
        vida_anterior_j1 = jugador_1.vida
        jugador_2.atacar(jugador_1)
        daño = vida_anterior_j1 - jugador_1.vida
        daño_total_j2 += daño
        
        turno = turno + 1

    print(f"\n{'='*60} ESTADÍSTICAS FINALES {'='*60}")
    print(f"\nTurno final: {turno}")
    print(f"{jugador_1.nombre}: {daño_total_j1} daño total realizado")
    print(f"{jugador_2.nombre}: {daño_total_j2} daño total realizado")
    
    if jugador_1.esta_vivo():
        print(f"\n🏆 ¡GANADOR: {jugador_1.nombre}!")
    elif jugador_2.esta_vivo():
        print(f"\n🏆 ¡GANADOR: {jugador_2.nombre}!")
    else:
        print("\n⚖️  EMPATE")
