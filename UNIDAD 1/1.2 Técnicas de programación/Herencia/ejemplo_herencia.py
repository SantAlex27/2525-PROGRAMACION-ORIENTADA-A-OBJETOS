# Ejemplo de Herencia

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada


# Uso
m1 = Moto("Yamaha", "R3", 321)
print(m1.marca, m1.modelo, m1.cilindrada)
