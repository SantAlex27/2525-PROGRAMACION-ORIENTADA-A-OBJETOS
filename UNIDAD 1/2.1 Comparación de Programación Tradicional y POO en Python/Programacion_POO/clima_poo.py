# Programación Orientada a Objetos (POO)
# Promedio semanal del clima

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas de la semana:")
        for dia in range(1, 8):
            temp = float(input(f"Día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


if __name__ == "__main__":
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"Promedio semanal: {promedio:.2f} °C")