# CASO DE MUNDO REAL: SISTEMA DE RESERVAS DE HOTEL
# Descripción: Este programa modela cómo un cliente reserva una habitación,
# demostrando la interacción entre dos clases distintas.

# ETIQUETA: Clase Habitación (Modela el objeto físico)
class Habitacion:
    def __init__(self, numero, tipo, precio):
        # ETIQUETA: Atributos (Características)
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True  # Estado inicial disponible

    # ETIQUETA: Método (Acción del objeto)
    def ocupar(self):
        """Cambia el estado de la habitación a ocupada."""
        self.esta_disponible = False

    def __str__(self):
        estado = "Disponible" if self.esta_disponible else "Ocupada"
        return f"Hab {self.numero} ({self.tipo}) - ${self.precio} [{estado}]"


# ETIQUETA: Clase Reserva (Modela la lógica del negocio)
class Reserva:
    def __init__(self, nombre_cliente, habitacion_objeto):
        self.nombre_cliente = nombre_cliente
        # ETIQUETA: Atributo que recibe un objeto (Asociación)
        self.habitacion = habitacion_objeto

    # ETIQUETA: Interacción entre objetos
    def confirmar_reserva(self):
        """El objeto Reserva interactúa con el objeto Habitación."""
        if self.habitacion.esta_disponible:
            self.habitacion.ocupar()  # El objeto Reserva cambia el estado de Habitación
            print(f"Éxito: Reserva confirmada para {self.nombre_cliente}.")
        else:
            print(f"Error: La habitación {self.habitacion.numero} no está libre.")


# ETIQUETA: Ejecución del programa
if __name__ == "__main__":
    # Instanciación
    hab1 = Habitacion(101, "Suite", 120.0)

    print("Estado inicial:")
    print(hab1)

    # Creamos la reserva y ocurre la interacción
    reserva_santi = Reserva("Santi", hab1)
    reserva_santi.confirmar_reserva()

    print("\nEstado final tras la reserva:")
    print(hab1)