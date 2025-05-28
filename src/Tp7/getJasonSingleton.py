#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
getJasonSingleton.py

Programa para leer un archivo JSON y obtener una clave específica.

Copyright UADER-FCyT-IS2 ©2024 todos los derechos reservados.
Versión 1.1
"""

import json
import sys


class JsonReader:
    """
    Clase Singleton para lectura y extracción de claves de archivos JSON.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JsonReader, cls).__new__(cls)
        return cls._instance

    def read_key_from_file(self, filename, key):
        """
        Lee un archivo JSON y devuelve el valor de una clave específica.
        """
        try:
            with open(filename, "r", encoding="utf-8") as myfile:
                data = json.load(myfile)
        except FileNotFoundError:
            return f"Error: archivo '{filename}' no encontrado."
        except json.JSONDecodeError:
            return "Error: formato JSON inválido."
        except Exception as e:
            return f"Error inesperado: {str(e)}"

        if key in data:
            return str(data[key])
        return f"Clave '{key}' no encontrada en el archivo JSON."


def main():
    """
    Punto de entrada principal del programa.
    Valida argumentos y ejecuta la lectura segura del JSON.
    """
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("Versión 1.1")
        return

    if len(sys.argv) < 2:
        print("Uso: python getJason.py archivo.json [clave]")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) >= 3 else "token1"

    reader = JsonReader()
    result = reader.read_key_from_file(jsonfile, jsonkey)
    print(result)


if __name__ == "__main__":
    main()
