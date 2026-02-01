"""
FUNCIONALIDAD: Programa principal de conversión de temperatura.
Este programa utiliza modularidad al importar funciones de 'calculos.py'
y demuestra el uso de tipos de datos: string, float, integer y boolean.
"""

# Importamos las funciones desde nuestro otro archivo (Modularidad)
from calculos import convertir_celsius_a_fahrenheit, es_temperatura_congelacion


def ejecutar_sistema():
    # 1. TIPO DE DATOS: String (Cadena de texto)
    nombre_usuario = "Usuario de Python"
    print(f"--- Bienvenido {nombre_usuario} al conversor modular ---")

    try:
        # 2. TIPO DE DATOS: Float (Punto flotante)
        # Pedimos el dato y lo convertimos a decimal para hacer cálculos
        entrada = input("Por favor, ingrese la temperatura en grados Celsius: ")
        celsius = float(entrada)

        # LLAMADA MODULAR: Usamos las funciones del archivo calculos.py
        fahrenheit = convertir_celsius_a_fahrenheit(celsius)

        # 3. TIPO DE DATOS: Boolean (Booleano)
        congelado = es_temperatura_congelacion(celsius)

        # 4. TIPO DE DATOS: Integer (Entero)
        # Convertimos el resultado a entero para mostrar otra forma de dato
        fahrenheit_entero = int(fahrenheit)

        # SALIDA DE DATOS: Mostramos todo de forma clara
        print("\n=== REPORTE DE RESULTADOS ===")
        print(f"Temperatura original: {celsius}°C")
        print(f"Conversión exacta: {fahrenheit}°F (Tipo: Float)")
        print(f"Valor redondeado: {fahrenheit_entero}°F (Tipo: Integer)")
        print(f"¿Se encuentra en estado de congelación?: {congelado} (Tipo: Boolean)")

    except ValueError:
        # Manejo de errores por si el usuario no ingresa un número
        print("Error: El valor ingresado no es un número válido.")


# Punto de inicio del programa
if __name__ == "__main__":
    ejecutar_sistema()