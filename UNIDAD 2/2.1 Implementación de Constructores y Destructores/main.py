from servicios.gestion_datos import ServicioDatos


def flujo_principal():
    # Instanciamos el servicio (esto no dispara destructores de modelos aún)
    gestor = ServicioDatos()

    print("DEMOSTRACIÓN DE CICLO DE VIDA EN POO")

    # CASO A: Destrucción automática al terminar el alcance (scope)
    # Verás que el destructor se activa justo cuando termina el método 'procesar_informacion'
    gestor.procesar_informacion("reporte_mensual.txt")

    print("-" * 50)

    # CASO B: Destrucción manual provocada por el usuario
    print("CASO MANUAL: Creando objeto en el flujo principal...")
    from modelos.base_datos import ConexionDatos
    conexion_manual = ConexionDatos("Base_de_Datos_Principal")

    print("Forzando la eliminación del objeto ahora mismo...")
    # Usar 'del' fuerza la llamada inmediata al destructor __del__
    del conexion_manual

    print("\n FIN DEL PROGRAMA ")


if __name__ == "__main__":
    flujo_principal()