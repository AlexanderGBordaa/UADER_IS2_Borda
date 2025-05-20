import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python getJason.py archivo.json [clave]")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) >= 3 else 'token1'

    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        if jsonkey in obj:
            print(str(obj[jsonkey]))
        else:
            print(f"Clave '{jsonkey}' no encontrada en el archivo JSON.")
    except FileNotFoundError:
        print(f"Archivo '{jsonfile}' no encontrado.")
    except json.JSONDecodeError:
        print("Error al parsear el archivo JSON.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
