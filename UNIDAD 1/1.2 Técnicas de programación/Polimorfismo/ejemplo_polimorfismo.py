# Ejemplo de Polimorfismo

class Vehiculo:
    def descripcion(self):
        return "Soy un vehículo"

class Auto(Vehiculo):
    def descripcion(self):
        return "Soy un auto"

class Moto(Vehiculo):
    def descripcion(self):
        return "Soy una moto"


# Uso
vehiculos = [Vehiculo(), Auto(), Moto()]

for v in vehiculos:
    print(v.descripcion())   # polimorfismo
