# Ejemplo de Abstracción

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.marca} {self.modelo}"


# Uso
v1 = Vehiculo("Toyota", "Corolla")
print(v1.descripcion())
