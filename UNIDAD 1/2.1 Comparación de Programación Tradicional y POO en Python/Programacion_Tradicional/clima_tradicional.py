# Programación Tradicional
# Promedio semanal del clima

def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de la semana:")
    for dia in range(1, 8):
        temp = float(input(f"Día {dia}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


if __name__ == "__main__":
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"Promedio semanal: {promedio:.2f} °C")