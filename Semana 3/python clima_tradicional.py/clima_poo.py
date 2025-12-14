"""
PROGRAMA: Cálculo de Promedio Semanal de Temperatura - Programación Orientada a Objetos
Autor: Jairo Estiven Sayay Alvarez
Descripción: Este programa utiliza POO para calcular el promedio semanal de temperaturas,
             aplicando conceptos de encapsulamiento, métodos y atributos de clase.
"""

class ClimaDiario:
    """
    Clase que representa la información climática de un día específico.

    Atributos:
        dia (str): Nombre del día de la semana
        temperatura (float): Temperatura registrada en grados Celsius
    """

    def __init__(self, dia, temperatura=0.0):
        """
        Constructor de la clase ClimaDiario.

        Args:
            dia (str): Nombre del día de la semana
            temperatura (float): Temperatura del día (por defecto 0.0)
        """
        self.__dia = dia  # Atributo privado (encapsulamiento)
        self.__temperatura = temperatura  # Atributo privado (encapsulamiento)

    # Métodos getter y setter para encapsulamiento
    def get_dia(self):
        """Retorna el nombre del día."""
        return self.__dia

    def get_temperatura(self):
        """Retorna la temperatura del día."""
        return self.__temperatura

    def set_temperatura(self, temperatura):
        """
        Establece la temperatura del día.

        Args:
            temperatura (float): Nueva temperatura a asignar
        """
        self.__temperatura = temperatura

    def __str__(self):
        """
        Representación en cadena del objeto.

        Returns:
            str: Información formateada del día y su temperatura
        """
        return f"{self.__dia}: {self.__temperatura:.1f}°C"


class RegistroClimatico:
    """
    Clase que gestiona el registro semanal de temperaturas.

    Atributos:
        semana (list): Lista de objetos ClimaDiario
    """

    def __init__(self):
        """Constructor que inicializa el registro semanal."""
        self.__semana = []  # Lista privada de días (encapsulamiento)
        self.__dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", 
                             "Viernes", "Sábado", "Domingo"]
        self.__inicializar_semana()

    def __inicializar_semana(self):
        """Método privado para inicializar los 7 días de la semana."""
        for dia in self.__dias_semana:
            self.__semana.append(ClimaDiario(dia))

    def ingresar_temperaturas(self):
        """
        Solicita al usuario ingresar las temperaturas diarias.
        Implementa validación de entrada para evitar errores.
        """
        print("\n=== INGRESO DE TEMPERATURAS SEMANALES ===\n")

        for clima_dia in self.__semana:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {clima_dia.get_dia()} (°C): "))
                    clima_dia.set_temperatura(temp)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un número válido.\n")

    def calcular_promedio(self):
        """
        Calcula el promedio de temperaturas de la semana.

        Returns:
            float: Promedio semanal de temperaturas
        """
        if len(self.__semana) == 0:
            return 0.0

        suma_temperaturas = sum(dia.get_temperatura() for dia in self.__semana)
        promedio = suma_temperaturas / len(self.__semana)

        return promedio

    def obtener_temperatura_maxima(self):
        """
        Obtiene la temperatura máxima de la semana.

        Returns:
            tuple: (día, temperatura máxima)
        """
        dia_max = max(self.__semana, key=lambda d: d.get_temperatura())
        return dia_max.get_dia(), dia_max.get_temperatura()

    def obtener_temperatura_minima(self):
        """
        Obtiene la temperatura mínima de la semana.

        Returns:
            tuple: (día, temperatura mínima)
        """
        dia_min = min(self.__semana, key=lambda d: d.get_temperatura())
        return dia_min.get_dia(), dia_min.get_temperatura()

    def mostrar_resultados(self):
        """Muestra un resumen completo del análisis climático semanal."""
        print("\n" + "="*55)
        print("RESULTADOS DEL ANÁLISIS CLIMÁTICO SEMANAL")
        print("="*55)

        # Mostrar temperaturas diarias
        print("\nTemperaturas registradas:")
        for clima_dia in self.__semana:
            print(f"  {clima_dia}")

        # Calcular y mostrar estadísticas
        promedio = self.calcular_promedio()
        dia_max, temp_max = self.obtener_temperatura_maxima()
        dia_min, temp_min = self.obtener_temperatura_minima()

        print("\n" + "-"*55)
        print("ESTADÍSTICAS:")
        print(f"  • Promedio semanal: {promedio:.2f}°C")
        print(f"  • Temperatura máxima: {temp_max:.1f}°C ({dia_max})")
        print(f"  • Temperatura mínima: {temp_min:.1f}°C ({dia_min})")
        print("="*55)


def main():
    """
    Función principal que ejecuta el sistema de registro climático.
    """
    print("\n*** SISTEMA DE REGISTRO CLIMÁTICO SEMANAL (POO) ***")

    # Crear instancia del registro climático
    registro = RegistroClimatico()

    # Ingresar datos
    registro.ingresar_temperaturas()

    # Mostrar resultados y análisis
    registro.mostrar_resultados()


# Punto de entrada del programa
if __name__ == "__main__":
    main()