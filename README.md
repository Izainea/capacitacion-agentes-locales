# Capacitación: Agentes Locales con Ollama y LangChain

Taller práctico para construir agentes de IA que corren **100% en tu máquina**, sin depender de APIs externas ni enviar datos a la nube. Usamos modelos de lenguaje locales a través de [Ollama](https://ollama.com/) y orquestamos agentes con [LangChain](https://www.langchain.com/).

## ¿Por qué agentes locales?

- **Privacidad**: Los datos nunca salen de tu máquina
- **Sin costos recurrentes**: No pagas por tokens ni llamadas API
- **Sin conexión**: Funciona offline una vez descargados los modelos
- **Control total**: Elige el modelo, ajusta parámetros, sin restricciones externas

## Requisitos previos

### Hardware mínimo
- 8 GB de RAM (16 GB recomendado)
- 5 GB de disco libre para modelos
- GPU opcional (acelera inferencia pero no es obligatorio)

### Software
- Python 3.11+
- [Ollama](https://ollama.com/) instalado y corriendo
- Git

### Verificar instalación de Ollama

```bash
# Verificar que Ollama está instalado
ollama --version

# Descargar los modelos que usaremos en el taller
ollama pull gemma3:27b
ollama pull gemma3:12b
ollama pull nomic-embed-text
```

## Instalación del taller

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/capacitacion-agentes-locales.git
cd capacitacion-agentes-locales

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Copiar configuración
cp .env.example .env
```

## Estructura del taller

El taller se divide en 5 notebooks progresivos:

| # | Notebook | Tema | Duración |
|---|----------|------|----------|
| 01 | [Hola Ollama](notebooks/01_hola_ollama.ipynb) | Conexión básica a Ollama desde Python | 30 min |
| 02 | [LangChain Básico](notebooks/02_langchain_basico.ipynb) | Chains, prompts y modelos con LangChain | 45 min |
| 03 | [Herramientas y Agentes](notebooks/03_herramientas_agentes.ipynb) | Crear herramientas propias y agentes que las usan | 60 min |
| 04 | [RAG Local](notebooks/04_rag_local.ipynb) | Retrieval Augmented Generation con documentos locales | 60 min |
| 05 | [Agente Completo](notebooks/05_agente_completo.ipynb) | Agente con memoria, herramientas y RAG integrado | 45 min |

## Estructura del repositorio

```
capacitacion-agentes-locales/
├── notebooks/          # Notebooks del taller (01-05)
├── src/                # Módulos reutilizables
│   ├── tools.py        # Herramientas personalizadas para agentes
│   └── utils.py        # Utilidades (conexión Ollama, helpers)
├── examples/           # Scripts de ejemplo independientes
│   └── agente_simple.py
├── assets/             # Imágenes y recursos del taller
├── requirements.txt    # Dependencias Python
├── .env.example        # Variables de entorno de ejemplo
├── .gitignore
└── README.md
```

## Modelos recomendados

| Modelo | Tamaño | Uso |
|--------|--------|-----|
| `gemma3:27b` | ~17 GB | Modelo principal (razonamiento complejo) |
| `gemma3:12b` | ~8 GB | Alternativa mas rapida |
| `nomic-embed-text` | ~275 MB | Embeddings para RAG (notebook 04) |

Para descargar cualquier modelo:
```bash
ollama pull nombre-del-modelo
```

## Conceptos clave

### ¿Qué es un Agente?
Un agente es un sistema que usa un LLM como "cerebro" para decidir qué acciones tomar. A diferencia de un chatbot simple, un agente puede:
- Usar **herramientas** (buscar archivos, hacer cálculos, consultar bases de datos)
- **Razonar** sobre qué herramienta usar y cuándo
- Mantener **memoria** de la conversación
- **Iterar** hasta resolver la tarea

### Flujo de un Agente
```
Usuario → Pregunta → LLM (decide) → Herramienta → Resultado → LLM (evalúa) → Respuesta
                         ↑                                          |
                         └──────────── (itera si necesita) ─────────┘
```

## Solución de problemas

### Ollama no responde
```bash
# Verificar que el servicio está corriendo
systemctl status ollama    # Linux con systemd
ollama serve               # Iniciar manualmente
```

### Modelo muy lento
- Si gemma3:27b es lento, usa gemma3:12b que es mas rapido
- Cierra otras aplicaciones para liberar RAM
- Si tienes GPU NVIDIA, verifica que Ollama la detecta: `ollama ps`

### Error de conexión
Verifica que Ollama está en el puerto por defecto:
```bash
curl http://localhost:11434/api/tags
```

## Recursos adicionales

- [Documentación de Ollama](https://github.com/ollama/ollama/blob/main/docs/README.md)
- [Documentación de LangChain](https://python.langchain.com/docs/introduction/)
- [Modelos disponibles en Ollama](https://ollama.com/library)

## Licencia

MIT
