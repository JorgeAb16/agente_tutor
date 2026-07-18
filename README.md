# Agente Tutor de Inteligencia Artificial

Agente tutor capaz de explicar temas de Inteligencia Artificial adaptando el nivel de la explicación al usuario (principiante, intermedio o avanzado), generando además un ejemplo práctico y una pregunta de evaluación. El modelo de lenguaje se ejecuta mediante una API compatible con OpenAI (LM Studio en local, o Hugging Face Inference Providers en producción), y la interfaz está construida con Streamlit.

## Tecnologías utilizadas

- **Python** — lenguaje base del proyecto
- **Streamlit** — interfaz web interactiva
- **Agno** — framework de orquestación del agente
- **LM Studio** — ejecución local del modelo (desarrollo)
- **Qwen2.5-VL-3B-Instruct** — modelo de lenguaje multimodal
- **Hugging Face Inference Providers** — API en la nube para el despliegue
- **python-dotenv** — manejo de variables de entorno

## Estructura del proyecto

```
agno/
├── app.py             # Interfaz principal en Streamlit
├── agente.py          # Lógica del agente y conexión con el modelo
├── requirements.txt   # Dependencias del proyecto
├── .env                # Variables de entorno (no incluir credenciales reales)
└── README.md           # Este archivo
```

## Requisitos previos

- Python 3.10 o superior
- [LM Studio](https://lmstudio.ai/) instalado (para ejecución local del modelo)
- Una cuenta de [Hugging Face](https://huggingface.co/) con un token de acceso (para el despliegue en la nube)

## Instalación

1. Clonar o descomprimir el proyecto y ubicarse en la carpeta:
   ```bash
   cd agno
   ```

2. Crear el entorno virtual:
   ```bash
   python -m venv venv
   ```

3. Activar el entorno virtual:
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

4. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración de variables de entorno

Crea un archivo `.env` en la raíz del proyecto (puedes basarte en `.env.example` si está incluido) con las siguientes variables:

```env
LM_STUDIO_BASE_URL=http://127.0.0.1:1234/v1
LM_STUDIO_API_KEY=lm-studio
LM_STUDIO_MODEL=qwen2.5-vl-3b-instruct
```

> ⚠️ **Nunca subas tu `.env` con credenciales reales a un repositorio público.** Asegúrate de que esté incluido en `.gitignore`.

### Opción A — Modelo local con LM Studio (desarrollo)

1. Abre LM Studio y descarga el modelo **Qwen2.5-VL-3B-Instruct**.
2. Ve a **Developer → Server Settings** y habilita el servidor local.
3. Copia el puerto y la URL que muestra LM Studio (puede cambiar en cada reinicio) y actualiza `LM_STUDIO_BASE_URL` en tu `.env`.
4. Si tienes la autenticación activada, genera un token en LM Studio y colócalo en `LM_STUDIO_API_KEY`. Si está desactivada, cualquier valor no vacío (ej. `lm-studio`) funciona.

### Opción B — Modelo en la nube con Hugging Face (despliegue)

1. Genera un token en [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) con permiso **"Make calls to Inference Providers"**.
2. Actualiza tu `.env`:
   ```env
   LM_STUDIO_BASE_URL=https://router.huggingface.co/v1
   LM_STUDIO_API_KEY=hf_tu_token_aqui
   LM_STUDIO_MODEL=Qwen/Qwen2.5-VL-3B-Instruct:featherless-ai
   ```

## Ejecución local

Con el entorno virtual activado y el `.env` configurado:

```bash
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`.

## Despliegue en Streamlit Community Cloud

1. Sube el proyecto a un repositorio de GitHub (sin el `.env` real, sin `venv/` ni `__pycache__/`).
2. Conecta el repositorio en [share.streamlit.io](https://share.streamlit.io).
3. En **Settings → Secrets**, agrega las variables de entorno en formato TOML:
   ```toml
   LM_STUDIO_BASE_URL = "https://router.huggingface.co/v1"
   LM_STUDIO_API_KEY = "hf_tu_token_aqui"
   LM_STUDIO_MODEL = "Qwen/Qwen2.5-VL-3B-Instruct:featherless-ai"
   ```
4. Guarda los cambios y espera a que la app se reinicie (~1 minuto).

> Streamlit Cloud no puede acceder a un servidor `localhost`, por eso el despliegue público usa Hugging Face Inference Providers en lugar de LM Studio.

## Uso

1. Selecciona un tema de Inteligencia Artificial.
2. Elige el nivel de explicación (principiante, intermedio o avanzado).
3. El agente generará:
   - Una explicación adaptada al nivel seleccionado.
   - Un ejemplo práctico relacionado con el tema.
   - Una pregunta de evaluación para reforzar el aprendizaje.

## Notas y lecciones aprendidas

- Al reiniciar LM Studio, el puerto del servidor local puede cambiar; siempre verifica la URL activa antes de ejecutar la app.
- Un error `401 - Invalid API Key` generalmente indica un problema de configuración de autenticación en el servidor (LM Studio) o un token inválido/revocado (Hugging Face), no necesariamente un error en el código del agente.
- Nunca se deben exponer tokens de API en el código fuente ni en capturas de pantalla; siempre deben manejarse mediante variables de entorno o el gestor de secretos de la plataforma de despliegue.

## Autor

Jorge Abraham Fajardo — Inteligencía Artificial — Julio 2026
