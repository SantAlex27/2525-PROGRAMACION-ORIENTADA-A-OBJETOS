# Sistema de Gestión de Conexiones (POO)

Este programa demuestra el ciclo de vida de un objeto en Python utilizando **Constructores** y **Destructores**.

## Arquitectura
- **Modelos**: Contiene la clase `ConexionDatos` que simula la apertura y cierre de recursos.
- **Servicios**: Contiene `ServicioDatos` que gestiona la lógica de uso de las conexiones.
- **Main**: Punto de entrada que orquesta el flujo.

## Uso de __init__ y __del__
- El **Constructor (`__init__`)** se usa para establecer el nombre del recurso y marcar la conexión como activa.
- El **Destructor (`__del__`)** asegura que, sin importar cuándo se elimine el objeto, la conexión se marque como cerrada, evitando fugas de memoria o recursos colgados.

## Cómo ejecutar
Ejecuta el archivo principal desde la raíz del proyecto:
```bash
python main.py