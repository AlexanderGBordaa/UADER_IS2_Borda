"""Un asistente interactivo que utiliza la API de Gemini."""
import os
import sys
import json
import google.generativeai as genai

# Intenta obtener la API key desde una variable de entorno, si no existe, usa la que tenías
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = "AIzaSyB_pfMVMLijz0Ojs56GIiTFIX-1HLfe58I"  # ¡Recuerda configurar la variable de entorno!
    print("Advertencia: Usando la API key directamente en el código. Se recomienda usar una variable de entorno.")

# Configura la API key de Gemini
genai.configure(api_key=API_KEY)

# Modelo a utilizar
model = genai.GenerativeModel('gemini-1.5-flash')

# Contexto inicial
CONTEXT = "Eres un asistente útil y amigable."
ULTIMA_CONSULTA = ""
CONVERSATION_HISTORY = [
    {"role": "user", "parts": [CONTEXT]}
]  # Mantener el contexto inicial en el historial

def obtener_consulta_usuario():
    """Gestiona la aceptación de la consulta del usuario con historial."""
    global ULTIMA_CONSULTA
    try:
        if sys.stdin.isatty():
            readline_available = False
            try:
                import readline
                readline_available = True
            except ImportError:
                try:
                    import pyreadline3 as readline
                    readline_available = True
                except ImportError:
                    pass  # No se pudo importar ninguna librería de readline

            if readline_available:
                readline.set_history_length(10)
                if ULTIMA_CONSULTA:
                    readline.add_history(ULTIMA_CONSULTA)
                consulta = input("Ingresa tu consulta (o cursor Up para editar la anterior): ")
                if consulta:
                    ULTIMA_CONSULTA = consulta
                return consulta
            else:
                consulta = input("Ingresa tu consulta: ")
                if consulta:
                    ULTIMA_CONSULTA = consulta
                return consulta
        else:
            consulta = input("Ingresa tu consulta: ")
            if consulta:
                ULTIMA_CONSULTA = consulta
            return consulta
    except Exception as e:
        print(f"Error al obtener la consulta del usuario: {e}")
        return None

def procesar_consulta(userquery):
    """Gestiona el procesamiento de la consulta del usuario y actualiza el historial."""
    global CONVERSATION_HISTORY
    try:
        if userquery and userquery.strip():
            print(f"You: {userquery}")
            CONVERSATION_HISTORY.append({"role": "user", "parts": [userquery]})
            return CONVERSATION_HISTORY
        print("La consulta del usuario está vacía.")
        return None
    except Exception as e:
        print(f"Error al procesar la consulta: {e}")
        return None

def invocar_gemini(conversation_history):
    """Gestiona la invocación de la API de Gemini utilizando el historial de la conversación."""
    try:
        if conversation_history:
            response = model.generate_content(conversation_history)
            return response
        return None
    except genai.GenerativeModelError as e:
        print(f"Error específico de Gemini: {e}")
        return None
    except Exception as e:
        print(f"Error al invocar la API de Gemini: {e}")
        return None

def mostrar_respuesta_gemini(response):
    """Muestra la respuesta de Gemini al usuario."""
    if response and response.parts:
        gemini_response = response.parts[0].text
        print(f"Gemini: {gemini_response}")
        global CONVERSATION_HISTORY
        CONVERSATION_HISTORY.append({"role": "model", "parts": [gemini_response]})
    elif response:
        print("La respuesta de Gemini está vacía.")
    else:
        print("No se recibió respuesta de Gemini.")

# Programa principal
if __name__ == "__main__":
    try:
        while True:
            consulta = obtener_consulta_usuario()
            if consulta is None:
                break
            if consulta.lower() == 'salir':
                break

            conversation = procesar_consulta(consulta)
            if conversation:
                respuesta = invocar_gemini(conversation)
                mostrar_respuesta_gemini(respuesta)

    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
    except Exception as e:
        print(f"Error general en la ejecución del programa: {e}")
    finally:
        print("Saliendo del asistente.")

print()