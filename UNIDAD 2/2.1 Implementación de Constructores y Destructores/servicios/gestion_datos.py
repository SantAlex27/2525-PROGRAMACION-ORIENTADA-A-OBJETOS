from modelos.base_datos import ConexionDatos


class ServicioDatos:
    def procesar_informacion(self, nombre_archivo):
        """
        Este servicio gestiona la creación y el uso del modelo.
        """
        print(f"\n>> SERVICIO: Iniciando procesamiento de {nombre_archivo}...")

        # 1. Al crear esta instancia, se dispara automáticamente el __init__ de ConexionDatos
        conexion = ConexionDatos(nombre_archivo)

        # 2. Realizamos alguna operación lógica
        print(f">> SERVICIO: Trabajando con los datos de {conexion.nombre_recurso}...")

        # 3. Al terminar este método, la variable 'conexion' deja de existir (sale de ámbito).
        # Python llamará al DESTRUCTOR (__del__) automáticamente después de este punto.
        print(f">> SERVICIO: Finalizando tarea de {nombre_archivo}.\n")