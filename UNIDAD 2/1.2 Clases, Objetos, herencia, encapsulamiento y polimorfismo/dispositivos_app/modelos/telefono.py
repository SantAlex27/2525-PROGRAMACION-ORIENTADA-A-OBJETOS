from modelos.dispositivo import Dispositivo

# Herencia: Telefono hereda de Dispositivo
class Telefono(Dispositivo):
    def __init__(self, marca, modelo, precio, operador):
        super().__init__(marca, modelo, precio)
        self.operador = operador

    # Polimorfismo: Sobrescribimos el método mostrar_detalle
    def mostrar_detalle(self):
        detalle_base = super().mostrar_detalle()
        return f"{detalle_base} | Operador: {self.operador} | Tipo: Teléfono"