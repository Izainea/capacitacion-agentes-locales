"""Herramientas reutilizables para agentes."""

import math
import datetime
import os
from langchain_core.tools import tool


@tool
def calculadora(expresion: str) -> str:
    """Evalúa una expresión matemática. Ejemplo: '2 + 2', 'math.sqrt(16)', '1500 * 3.5 / 60'"""
    try:
        resultado = eval(expresion, {"math": math, "__builtins__": {}})
        return f"Resultado: {resultado}"
    except Exception as e:
        return f"Error en el cálculo: {e}"


@tool
def fecha_hora() -> str:
    """Devuelve la fecha y hora actual del sistema."""
    ahora = datetime.datetime.now()
    return ahora.strftime("Hoy es %A %d de %B de %Y, son las %H:%M")


@tool
def listar_archivos(directorio: str) -> str:
    """Lista los archivos en un directorio del sistema."""
    try:
        archivos = os.listdir(directorio)
        if not archivos:
            return f"El directorio '{directorio}' está vacío."
        return f"Archivos en '{directorio}':\n" + "\n".join(
            f"  - {a}" for a in sorted(archivos)
        )
    except FileNotFoundError:
        return f"El directorio '{directorio}' no existe."


@tool
def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo de texto (máximo 2000 caracteres)."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read(2000)
        return contenido
    except FileNotFoundError:
        return f"El archivo '{ruta}' no existe."
    except Exception as e:
        return f"Error al leer: {e}"


@tool
def contar_palabras(texto: str) -> str:
    """Cuenta las palabras, oraciones y caracteres de un texto."""
    palabras = len(texto.split())
    oraciones = texto.count(".") + texto.count("!") + texto.count("?")
    caracteres = len(texto)
    return f"Palabras: {palabras}, Oraciones: {oraciones}, Caracteres: {caracteres}"
