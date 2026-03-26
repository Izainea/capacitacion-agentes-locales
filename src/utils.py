"""Utilidades para la capacitación de agentes locales."""

import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama, OllamaEmbeddings

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:12b")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")


def get_llm(model: str | None = None, temperature: float = 0) -> ChatOllama:
    """Crea una instancia de ChatOllama con la configuración del .env."""
    return ChatOllama(
        model=model or OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=temperature,
    )


def get_embeddings(model: str | None = None) -> OllamaEmbeddings:
    """Crea una instancia de OllamaEmbeddings con la configuración del .env."""
    return OllamaEmbeddings(
        model=model or OLLAMA_EMBED_MODEL,
        base_url=OLLAMA_BASE_URL,
    )


def verificar_ollama() -> bool:
    """Verifica que Ollama esté corriendo y muestra los modelos disponibles."""
    import requests

    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=5)
        modelos = response.json().get("models", [])
        print(f"Ollama corriendo en {OLLAMA_BASE_URL}")
        print(f"Modelos disponibles: {len(modelos)}")
        for m in modelos:
            print(f"  - {m['name']}")
        return True
    except requests.ConnectionError:
        print(f"ERROR: No se pudo conectar a Ollama en {OLLAMA_BASE_URL}")
        print("Ejecuta: ollama serve")
        return False
