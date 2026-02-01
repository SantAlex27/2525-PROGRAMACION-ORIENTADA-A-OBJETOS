from modelos.dispositivo import Dispositivo

class Computadora(Dispositivo):
    def __init__(self, marca, modelo, precio, ram):
        super().__init__(marca, modelo, precio)
        self.ram = ram

    # Polimorfismo: Otra implementación del mismo método
    def mostrar_detalle(self):
        detalle_base = super().mostrar_detalle()
        return f"{detalle_base} | RAM: {self.ram}GB | Tipo: Computadora"