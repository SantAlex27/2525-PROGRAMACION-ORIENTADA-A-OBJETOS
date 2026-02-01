"""
DESCRIPCIÓN: Módulo de lógica matemática.
Este archivo contiene las funciones que procesan los datos numéricos.
"""

# Definimos una función con un identificador descriptivo en snake_case
def convertir_celsius_a_fahrenheit(valor_celsius):
    """
    TOMA: Un número decimal (float).
    HACE: Aplica la fórmula matemática de conversión.
    RETORNA: El resultado en grados Fahrenheit.
    """
    # Usamos una variable local con nombre claro
    # El dato aquí sigue siendo de tipo 'float' (decimal)
    resultado_f = (valor_celsius * 1.8) + 32
    return resultado_f

def es_temperatura_congelacion(valor_celsius):
    """
    TOMA: Un número decimal (float).
    HACE: Compara si el valor es menor o igual a 0.
    RETORNA: Un tipo de dato 'boolean' (True o False).
    """
    # Esta operación lógica genera un valor Booleano
    esta_congelado = valor_celsius <= 0
    return esta_congelado