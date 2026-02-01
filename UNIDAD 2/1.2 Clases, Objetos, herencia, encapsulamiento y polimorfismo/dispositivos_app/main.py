from modelos.telefono import Telefono
from modelos.computadora import Computadora
from servicios.inventario import Inventario

def ejecutar():
    # Instanciamos el servicio
    mi_inventario = Inventario()

    # Creamos objetos (Instanciación)
    tel = Telefono("Samsung", "S23", 800, "Movistar")
    pc = Computadora("Apple", "MacBook Pro", 2000, 16)

    # Agregamos al inventario
    mi_inventario.agregar_dispositivo(tel)
    mi_inventario.agregar_dispositivo(pc)

    # Mostramos resultados
    mi_inventario.mostrar_inventario()

if __name__ == "__main__":
    ejecutar()