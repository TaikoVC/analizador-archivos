import os
import sys

"""Revision del codigo"""""

def contar_lineas(contenido):
    """Cuenta el número de líneas en el contenido."""
    return len(contenido.splitlines())

def contar_palabras(contenido):
    """Cuenta el número de palabras en el contenido."""
    return len(contenido.split())

def contar_caracteres(contenido):
    """Cuenta el número de caracteres en el contenido."""
    return len(contenido)

def analizar_archivo(ruta_entrada, ruta_salida=None):
    """
    Lee un archivo de texto, calcula estadísticas y las guarda en un archivo de salida.
    Si no se especifica ruta_salida, imprime en consola.
    Lanza FileNotFoundError si el archivo no existe.
    """
    # Intentar abrir el archivo; si no existe, se lanza FileNotFoundError
    with open(ruta_entrada, 'r', encoding='utf-8') as f:
        contenido = f.read()

    lineas = contar_lineas(contenido)
    palabras = contar_palabras(contenido)
    caracteres = contar_caracteres(contenido)

    resultado = f"Archivo: {ruta_entrada}\n"
    resultado += f"Líneas: {lineas}\n"
    resultado += f"Palabras: {palabras}\n"
    resultado += f"Caracteres: {caracteres}\n"

    if ruta_salida:
        with open(ruta_salida, 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Resultados guardados en {ruta_salida}")
    else:
        print(resultado)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python analizador.py <archivo_entrada> [archivo_salida]")
        sys.exit(1)

    entrada = sys.argv[1]
    salida = sys.argv[2] if len(sys.argv) > 2 else None
    try:
        analizar_archivo(entrada, salida)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {entrada}")
        sys.exit(1)