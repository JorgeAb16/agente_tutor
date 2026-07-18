# Agente Tutor de Inteligencia Artificial

Proyecto educativo desarrollado con Agno, OpenAI y Streamlit.

## Objetivo

El estudiante escribe un tema y selecciona su nivel.

El agente debe:

- Explicar el tema de manera sencilla.
- Adaptar la explicación al nivel del estudiante.
- Presentar un ejemplo práctico.
- Crear una pregunta de evaluación.

## Requisitos

- Python 3.10 o superior.
- Una clave de la API de OpenAI.
- Conexión a Internet.

## Instalación

### 1. Crear el entorno virtual

```bash
python -m venv .venv

##activación
.venv\Scripts\activate

##keys open AI (PAGA)
https://platform.openai.com/api-keys

##Ejecutar el codigo
streamlit run app.py

## Con LM STUDIO
https://lmstudio.ai/ 

Buscar y descarga un modelo pequeño, por ejemplo:

Qwen2.5-3B-Instruct
Llama-3.2-3B-Instruct
Phi-3.5-mini-instruct

Carga el modelo.
Ve a la pestaña Developer.
Activa Start Server.


## Ejecuta el proyecto

Primero verifica que:

LM Studio esté abierto.
El modelo esté cargado.
El servidor local esté iniciado.
El puerto sea 1234.

Después ejecuta:

streamlit run app.py

Abre:

http://localhost:8501