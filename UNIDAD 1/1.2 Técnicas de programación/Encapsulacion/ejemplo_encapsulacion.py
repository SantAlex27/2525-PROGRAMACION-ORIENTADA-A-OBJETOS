# Ejemplo de Encapsulación

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self._marca = marca      # atributo protegido
        self._modelo = modelo
        self._año = año

    # Getters
    def get_marca(self):
        return self._marca

    # Setters
    def set_marca(self, nueva_marca):
        if len(nueva_marca) > 1:
            self._marca = nueva_marca


# Uso
v1 = Vehiculo("Honda", "Civic", 2020)
print(v1.get_marca())
v1.set_marca("Nissan")
print(v1.get_marca())
