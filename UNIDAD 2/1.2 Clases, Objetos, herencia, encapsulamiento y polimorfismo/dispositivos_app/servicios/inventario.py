class Inventario:
    def __init__(self):
        self.lista_dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.lista_dispositivos.append(dispositivo)
        print(f"Agregado: {dispositivo.marca} {dispositivo.modelo}")

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        for d in self.lista_dispositivos:
            # Aquí se ve el Polimorfismo en acción:
            # d.mostrar_detalle() se comporta diferente según el objeto
            print(f"{d.mostrar_detalle()} - Precio: ${d.obtener_precio()}")