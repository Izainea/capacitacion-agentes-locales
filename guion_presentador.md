# Guion del Presentador

## Antes de empezar (15 min antes)
- Verificar que Ollama esta corriendo: `ollama serve`
- Verificar modelos descargados: `ollama list`
- Abrir la presentacion en el navegador: `presentacion.html`
- Abrir JupyterLab con los notebooks listos
- Tener una terminal visible para demos en vivo

---

## Slide 1: Bienvenidos (5 min)

**Abrir con:**

> Bienvenidos a este taller. Hoy vamos a construir agentes de inteligencia artificial que corren completamente en nuestra maquina. Nada de lo que hagamos hoy va a enviar datos a la nube. Todo es local, todo es gratis, y todo funciona sin internet.

**Punto clave:**

> Cuando trabajamos con datos sensibles — como entrevistas, testimonios o datos personales — no podemos permitirnos enviar esa informacion a servidores de OpenAI o Google. Los modelos locales resuelven ese problema de raiz.

**Mostrar la comparacion cloud vs local y enfatizar:**

> Con APIs en la nube pagas por token, dependes de internet, y tus datos pasan por servidores ajenos. Con Ollama, descargas el modelo una vez y lo usas las veces que quieras, sin costo y sin conexion.

---

## Slide 2: Agenda del Taller (2 min)

> El taller tiene 5 modulos progresivos. Empezamos desde cero — conectarnos a Ollama — y terminamos con un agente completo que busca en documentos, hace calculos y recuerda la conversacion.

> Cada modulo tiene una parte teorica breve que veremos aqui en la presentacion, y luego vamos al notebook a practicar. La proporcion es mas o menos 30% teoria, 70% practica.

**Mencionar pausas:**

> Haremos pausas entre modulos. Si algo no funciona, me avisan y lo resolvemos en el momento.

---

## Slide 3: Que es Ollama (5 min)

> Ollama es como un Docker para modelos de lenguaje. Con un solo comando descargas un modelo y ya esta listo para usar. Corre como un servidor local en el puerto 11434.

**Demo en vivo en terminal:**

```bash
ollama list              # Mostrar modelos descargados
ollama run gemma3:12b      # Abrir chat directo y hacer una pregunta
# Escribir: "Que es un agente de IA? Responde en una oracion."
# Salir con /bye
```

> Ven? Asi de simple. Ollama maneja todo: la descarga, la carga en memoria, la inferencia. Nosotros solo le mandamos texto y recibimos texto.

**Repasar la tabla de modelos:**

> Para este taller usamos gemma3. Idealmente gemma3:27b para razonamiento complejo, pero gemma3:12b funciona bien si tienen menos RAM. Ademas necesitamos nomic-embed-text para embeddings.

---

## Slide 4: Que es LangChain (5 min)

> LangChain es el framework que nos permite conectar Ollama con herramientas, documentos y logica de negocio. Piensen en LangChain como el pegamento entre el modelo y todo lo demas.

**Explicar las 3 piezas clave:**

> Tres conceptos fundamentales:
> 1. **Prompt Templates**: plantillas con variables. En vez de concatenar strings, defines una plantilla y la llenas con datos.
> 2. **Chains**: encadenas operaciones con el operador pipe. Prompt entra, modelo procesa, parser formatea la salida.
> 3. **Salida estructurada**: puedes forzar al modelo a devolver JSON valido, no solo texto libre. Esto es crucial para automatizacion.

> **Ir al Notebook 01 y 02 ahora.** Vamos a ver esto en practica.

---

## [PRACTICA: Notebooks 01 y 02] (75 min)

### Notebook 01 - Hola Ollama (30 min)

Ejecutar celda por celda con los participantes:

1. **Verificar conexion**: Mostrar que Ollama responde y listar modelos
2. **Primera llamada**: Crear ChatOllama y enviar un mensaje simple
   > Noten que creamos una instancia de ChatOllama apuntando a gemma3:12b. La temperatura controla la creatividad.
3. **Streaming**: Mostrar como se ve la respuesta token por token
   > Esto es util para interfaces donde quieres que el usuario vea la respuesta mientras se genera.
4. **Mensajes con roles**: Explicar system, human, ai
   > El system message define la personalidad del modelo. Es como darle instrucciones de como comportarse.
5. **Parametros**: Comparar temperature 0 vs 1
   > Vean como con temperatura 0 siempre responde igual, y con temperatura 1 cada respuesta es diferente.

**Dar 5 min para el ejercicio al final.**

### Notebook 02 - LangChain Basico (45 min)

1. **Prompt Templates**: Crear plantilla con variables
   > Ya no concatenamos strings. Definimos la plantilla una vez y la reutilizamos con diferentes datos.
2. **Chains con LCEL**: Mostrar el operador pipe
   > Esto es lo mas elegante de LangChain. Prompt pipe modelo pipe parser. Tres lineas y tienes un pipeline completo.
3. **Salida estructurada**: Usar Pydantic para forzar JSON
   > Esto es poderoso. Definimos un modelo Pydantic y el LLM esta obligado a devolver exactamente esos campos. Nada de parsear texto a mano.
4. **Chains secuenciales**: Encadenar multiples llamadas
5. **Batch**: Procesar varias entradas

**Dar 5-10 min para el ejercicio.**

---

## Slide 5: Que es un Agente (5 min)

**Esta es la slide mas importante. Tomarse el tiempo.**

> Hasta ahora hemos usado el modelo como una caja que recibe texto y devuelve texto. Un agente es diferente: el modelo DECIDE que hacer.

**Usar la comparacion chatbot vs agente:**

> Un chatbot es como una enciclopedia: le preguntas y te responde con lo que sabe. Un agente es como un investigador: piensa que necesita, busca informacion, analiza lo que encontro, y si no es suficiente, busca mas.

**Explicar el flujo ReAct:**

> El ciclo es: el usuario pregunta, el LLM razona ("necesito la calculadora"), ejecuta la herramienta, observa el resultado, y decide si necesita mas o si puede responder.

> Enfaticen esto: el LLM NO ejecuta codigo. El LLM dice "quiero usar la calculadora con estos parametros". El sistema ejecuta y le devuelve el resultado.

---

## Slide 6: Herramientas (5 min)

> Las herramientas son funciones Python normales con un decorador @tool. Lo que las hace especiales es el docstring: ahi le decimos al modelo CUANDO usar esta herramienta.

**Enfatizar:**

> Un buen docstring es la diferencia entre un agente que funciona y uno que no. Si el docstring dice "Evalua una expresion matematica, usala para hacer calculos", el modelo sabra que cuando le pregunten "cuanto es 2+2" debe usar esta herramienta.

> Noten que los parametros tienen tipos. Esto le dice al modelo que argumentos enviar. Y el retorno siempre es string porque el modelo lee texto.

---

## Slide 7: Construir un Agente (3 min)

> Con todo lo anterior, crear el agente son 5 lineas. create_react_agent recibe el modelo, las herramientas y un prompt de sistema. Eso es todo.

> **Ir al Notebook 03 ahora.**

---

## [PRACTICA: Notebook 03] (60 min)

### Notebook 03 - Herramientas y Agentes

1. **Crear herramientas**: Definir calculadora, fecha_actual, diccionario
   > Prueben cada herramienta directamente con .invoke() para verificar que funciona.
2. **Bind tools**: Mostrar como el modelo "sabe" que tiene herramientas
   > Noten el campo tool_calls en la respuesta. El modelo no responde directamente, dice "quiero usar la calculadora".
3. **Crear agente ReAct**: Construir el agente
   > Ahora si, el agente completo. Preguntenmle algo que requiera dos herramientas y vean como las usa secuencialmente.
4. **Prompt personalizado**: Darle personalidad al agente
5. **Herramientas de archivos**: Leer archivos del sistema
   > Esto demuestra que pueden darle al agente acceso a cualquier cosa: archivos, APIs, bases de datos.
6. **Memoria**: Agregar MemorySaver
   > Sin memoria, cada mensaje es independiente. Con MemorySaver, el agente recuerda toda la conversacion.

**Dar 10 min para el ejercicio.**

**PAUSA (10 min)**

---

## Slide 8 y 9: RAG y Embeddings (10 min)

**Slide 8:**

> RAG resuelve un problema fundamental: los modelos solo saben lo que aprendieron en el entrenamiento. Si quieres que respondan sobre TUS documentos, necesitas RAG.

**Explicar los dos flujos con el diagrama:**

> Hay dos fases. Primero, indexacion: tomas tus documentos, los divides en fragmentos, calculas embeddings y los guardas en una base vectorial. Esto se hace una vez.
> Segundo, consulta: el usuario pregunta, conviertes la pregunta en embedding, buscas los fragmentos mas similares, y se los pasas al modelo junto con la pregunta.

**Slide 9:**

> El embedding es lo que hace posible la busqueda semantica. Convierte texto en numeros que capturan el significado.

**Usar el ejemplo de la tabla:**

> "El gato duerme en el sofa" y "el felino descansa en el mueble" tienen similitud 0.92 porque significan casi lo mismo, aunque no comparten palabras. En cambio, "Python es un lenguaje" tiene similitud 0.23 porque habla de algo completamente diferente.

> Esto es clave: la busqueda vectorial encuentra por significado, no por palabras exactas.

> **Ir al Notebook 04 ahora.**

---

## [PRACTICA: Notebook 04] (60 min)

### Notebook 04 - RAG Local

1. **Embeddings**: Mostrar como se ven los vectores y calcular similitud
   > Cada texto se convierte en un vector de 768 dimensiones. La similitud coseno mide que tan parecidos son.
2. **Documentos de ejemplo**: Crear documentos sobre Colombia
3. **Text Splitting**: Dividir documentos en fragmentos
   > Los modelos tienen limite de contexto. No puedes pasar un documento de 100 paginas. Lo divides en fragmentos de ~300 caracteres con superposicion.
4. **FAISS**: Crear base vectorial
   > FAISS guarda los vectores localmente. Es la libreria de Meta para busqueda eficiente de vectores.
5. **Busqueda por similitud**: Encontrar fragmentos relevantes
6. **RAG Chain**: Pregunta-busca-responde
   > Aqui esta la magia: el modelo responde SOLO con lo que encontro en los documentos. Si no hay informacion, dice que no sabe.
7. **PDFs reales** (si hay tiempo): Cargar un PDF real

**Dar 10 min para el ejercicio.**

---

## Slide 10: Agente Completo (5 min)

> En el ultimo notebook integramos todo. El agente tiene:
> - Un cerebro (gemma3:12b via Ollama)
> - Manos (herramientas: calculadora, archivos)
> - Conocimiento (RAG con FAISS)
> - Memoria (MemorySaver para recordar la conversacion)

> La busqueda RAG es simplemente otra herramienta. El agente decide cuando buscar en documentos, cuando usar la calculadora, o cuando responder directo.

> **Ir al Notebook 05 ahora.**

---

## [PRACTICA: Notebook 05] (45 min)

### Notebook 05 - Agente Completo

1. **Preparar base de conocimiento**: Crear vectorstore con documentos
2. **Definir herramientas**: buscar_documentos, calculadora, fecha, resumen
3. **Crear agente**: Con prompt especializado y memoria
4. **Conversacion de ejemplo**: Ejecutar las 4 preguntas de ejemplo
   > Observen como el agente decide que herramienta usar para cada pregunta. Para "que es la UBPD" busca en documentos. Para "cuantas paginas al ano" usa la calculadora.
5. **Chat interactivo**: Si hay tiempo, descomentar el loop

**Permitir exploracion libre los ultimos 10-15 min.**

---

## Slide 11: Proximos Pasos (3 min)

> Lo que vimos hoy es la base. A partir de aqui pueden:
> - Agregar herramientas mas complejas: SQL, APIs, web scraping
> - Montar una interfaz web con Streamlit para que otros usen el agente
> - Guardar la base vectorial en disco para no recalcular embeddings
> - Crear sistemas multi-agente donde varios agentes colaboran
> - Evaluar la calidad de las respuestas con metricas formales

---

## Slide 12: Recursos y Cierre (5 min)

> Todo el codigo esta en el repositorio. Los notebooks tienen ejercicios extra que pueden hacer por su cuenta.

**Cerrar con:**

> Lo mas importante que se llevan hoy: un modelo de lenguaje local + LangChain + herramientas propias = un agente que trabaja para ustedes, con sus datos, en su maquina. Experimentar es la mejor forma de aprender.

> Preguntas?

---

## Tips para el presentador

1. **Velocidad de inferencia**: Los modelos locales son mas lentos que APIs cloud. Si una celda tarda, explicar que es normal y aprovechar para dar contexto mientras espera.

2. **Errores comunes de los participantes**:
   - Ollama no esta corriendo: `ollama serve`
   - Modelo no descargado: `ollama pull gemma3:12b`
   - Puerto ocupado: Verificar con `curl http://localhost:11434`
   - Poca RAM: Usar `gemma3:12b` en vez de `gemma3:27b`

3. **Si un notebook falla**: Reiniciar el kernel y ejecutar desde el principio.

4. **Engagement**: Despues de cada demo en vivo, preguntar "Que creen que pasaria si...?" para generar discusion.

5. **Tiempo**: Si van cortos de tiempo, priorizar notebooks 01, 03 y 05. El 02 y 04 pueden asignarse como tarea.
