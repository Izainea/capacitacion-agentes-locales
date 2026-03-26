"""
Ejemplo: Agente simple con Ollama y LangChain.

Ejecutar:
    python examples/agente_simple.py

Requiere:
    - Ollama corriendo con el modelo gemma3:12b
    - pip install langchain-ollama langgraph
"""

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import math
import datetime


# --- Herramientas ---


@tool
def calculadora(expresion: str) -> str:
    """Evalúa una expresión matemática."""
    try:
        resultado = eval(expresion, {"math": math, "__builtins__": {}})
        return f"Resultado: {resultado}"
    except Exception as e:
        return f"Error: {e}"


@tool
def fecha_actual() -> str:
    """Devuelve la fecha y hora actual."""
    return datetime.datetime.now().strftime("%A %d de %B de %Y, %H:%M")


# --- Agente ---

llm = ChatOllama(model="gemma3:12b", temperature=0)

agente = create_react_agent(
    model=llm,
    tools=[calculadora, fecha_actual],
    prompt="Eres un asistente útil. Usa las herramientas cuando sea necesario. Responde en español.",
)


def main():
    print("Agente Simple con Ollama")
    print("Escribe 'salir' para terminar\n")

    while True:
        entrada = input("Tú: ").strip()
        if entrada.lower() in ("salir", "exit", "quit"):
            print("¡Hasta luego!")
            break
        if not entrada:
            continue

        resultado = agente.invoke({"messages": [("human", entrada)]})
        respuesta = resultado["messages"][-1].content
        print(f"Agente: {respuesta}\n")


if __name__ == "__main__":
    main()
