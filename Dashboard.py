import os
import subprocess


# Proyecto Adaptado con Navegación Profunda
# Estudiante: Santiago Vaca

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n{'=' * 20} VISTA PREVIA: {os.path.basename(ruta_script)} {'=' * 20}\n")
            print(codigo)
            return codigo
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    print(f"\n[SISTEMA]: Ejecutando {os.path.basename(ruta_script)}...")
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', f'"{ruta_script}"'])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', f'"{ruta_script}"'])
    except Exception as e:
        print(f"Error al ejecutar: {e}")


def listar_archivos_y_carpetas(ruta_actual):
    """
    Lista tanto archivos .py como carpetas para permitir navegación profunda.
    """
    objetos = os.scandir(ruta_actual)
    carpetas = []
    archivos = []

    for obj in objetos:
        if obj.is_dir() and not obj.name.startswith('__'):
            carpetas.append(obj.name)
        elif obj.is_file() and obj.name.endswith('.py') and obj.name != 'Dashboard.py':
            archivos.append(obj.name)

    return sorted(carpetas), sorted(archivos)


def navegar_recursivo(ruta_actual):
    while True:
        print(f"\n--- EXPLORANDO: {os.path.basename(ruta_actual) or ruta_actual} ---")
        carpetas, archivos = listar_archivos_y_carpetas(ruta_actual)

        opciones = {}
        contador = 1

        # Mostrar carpetas primero
        for carpeta in carpetas:
            print(f"{contador} - [CARPETA] {carpeta}")
            opciones[str(contador)] = ('dir', carpeta)
            contador += 1

        # Mostrar archivos después
        for archivo in archivos:
            print(f"{contador} - [ARCHIVO] {archivo}")
            opciones[str(contador)] = ('file', archivo)
            contador += 1

        print("0 - Regresar / Salir")

        eleccion = input("\nSeleccione una opción: ")

        if eleccion == '0':
            break
        elif eleccion in opciones:
            tipo, nombre = opciones[eleccion]
            nueva_ruta = os.path.join(ruta_actual, nombre)

            if tipo == 'dir':
                # Si es carpeta, entramos en ella (recursión)
                navegar_recursivo(nueva_ruta)
            else:
                # Si es archivo, mostramos y ejecutamos
                codigo = mostrar_codigo(nueva_ruta)
                if codigo:
                    ejecutar = input("\n¿Ejecutar script? (1: Sí / 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(nueva_ruta)
        else:
            print("\nOpción no válida.")


def mostrar_menu_principal():
    ruta_base = os.path.dirname(__file__)
    print("\n" + "=" * 40)
    print("  GESTOR DE PROYECTOS POO - MULTINIVEL")
    print("=" * 40)
    navegar_recursivo(ruta_base)


if __name__ == "__main__":
    mostrar_menu_principal()