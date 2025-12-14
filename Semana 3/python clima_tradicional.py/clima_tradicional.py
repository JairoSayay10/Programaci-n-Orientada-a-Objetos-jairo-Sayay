"""
PROGRAMA: Cálculo de Promedio Semanal de Temperatura - Programación Tradicional
Autor: Jairo Estiven Sayay Alvarez
Descripción: Este programa utiliza funciones para calcular el promedio semanal
             de temperaturas mediante programación estructurada tradicional.
"""

def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias de la semana.

    Returns:
        list: Lista con las temperaturas de los 7 días de la semana
    """
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("=== INGRESO DE TEMPERATURAS SEMANALES ===\n")

    for dia in dias_semana:
        while True:
            try:
                # Solicitar temperatura al usuario
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Ingrese un número válido.\n")

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.

    Args:
        temperaturas (list): Lista de temperaturas diarias

    Returns:
        float: Promedio de temperaturas
    """
    if len(temperaturas) == 0:
        return 0

    suma_total = sum(temperaturas)
    promedio = suma_total / len(temperaturas)

    return promedio


def mostrar_resultados(temperaturas, promedio):
    """
    Muestra los resultados del análisis de temperaturas.

    Args:
        temperaturas (list): Lista de temperaturas diarias
        promedio (float): Promedio calculado
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("\n" + "="*50)
    print("RESULTADOS DEL ANÁLISIS SEMANAL")
    print("="*50)

    # Mostrar temperaturas diarias
    print("\nTemperaturas registradas:")
    for i, dia in enumerate(dias_semana):
        print(f"  {dia}: {temperaturas[i]:.1f}°C")

    # Mostrar promedio
    print(f"\n>>> Promedio semanal: {promedio:.2f}°C")
    print("="*50)


def main():
    """
    Función principal que coordina la ejecución del programa.
    """
    print("\n*** SISTEMA DE REGISTRO CLIMÁTICO SEMANAL ***\n")

    # Paso 1: Ingresar datos
    temperaturas = ingresar_temperaturas()

    # Paso 2: Calcular promedio
    promedio = calcular_promedio(temperaturas)

    # Paso 3: Mostrar resultados
    mostrar_resultados(temperaturas, promedio)


# Punto de entrada del programa
if __name__ == "__main__":
    main()