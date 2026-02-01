class Dispositivo:
    def __init__(self, marca, modelo, precio):
        # Atributos protegidos y privados (Encapsulación)
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio  # Atributo privado con doble guion bajo

    # Método para obtener el precio (Getter)
    def obtener_precio(self):
        return self.__precio

    # Método común que será sobrescrito (Polimorfismo)
    def mostrar_detalle(self):
        return f"Dispositivo: {self.marca} {self.modelo}"