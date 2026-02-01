class ConexionDatos:
    def __init__(self, nombre_recurso):
        """
        CONSTRUCTOR (__init__):
        - Se ejecuta automáticamente al instanciar el objeto: 'obj = ConexionDatos()'
        - Propósito: Inicializar el estado del objeto y preparar recursos.
        """
        # Inicializamos atributos obligatorios recibidos por parámetro
        self.nombre_recurso = nombre_recurso
        # Definimos un estado inicial por defecto
        self.esta_conectado = True

        print(f"--- [EJECUCIÓN CONSTRUCTOR]: Se ha creado el objeto para '{self.nombre_recurso}'.")
        print(f"--- [INFO]: El estado inicial es CONECTADO.")

    def __del__(self):
        """
        DESTRUCTOR (__del__):
        - Se ejecuta cuando el objeto ya no tiene referencias o el programa finaliza.
        - Propósito: Limpieza de recursos (cerrar archivos, conexiones, logs).
        - Situación: Cuando se usa 'del obj' o cuando una función termina y su variable local muere.
        """
        # Simulamos la liberación de memoria o cierre de conexión
        self.esta_conectado = False
        print(f"--- [EJECUCIÓN DESTRUCTOR]: Liberando recursos de '{self.nombre_recurso}'.")
        print(f"--- [INFO]: Objeto eliminado exitosamente de la memoria.")