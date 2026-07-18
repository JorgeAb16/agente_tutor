import streamlit as st

from agente import crear_agente_tutor

st.set_page_config(
    page_title="Agente Tutor de IA",
    page_icon="",
    layout="centered",
)

st.title("🤖 Agente Tutor de Inteligencia Artificial")

st.write(
    "Escribe un tema, selecciona tu nivel y el agente lo explicará "
    "con un ejemplo y una pregunta de evaluación."
)

nivel = st.selectbox(
    "Selecciona el nivel del estudiante",
    ["Principiante", "Intermedio", "Avanzado"],
)

tema = st.text_input(
    "Tema que deseas aprender",
    placeholder="Ejemplo: aprendizaje supervisado",
)

if st.button("Explicar tema", type="primary"):
    if not tema.strip():
        st.warning("Escribe un tema antes de continuar.")
    else:
        mensaje = f"""
        Tema a explicar: {tema}
        Nivel del estudiante: {nivel}

        Genera una respuesta completa y específica sobre este tema para
        este nivel, siguiendo exactamente la estructura, el formato y las
        reglas de contenido que tienes definidas en tus instrucciones.
        Evita explicaciones genéricas que servirían para cualquier tema de
        IA: el ejemplo, la analogía y la pregunta deben estar claramente
        conectados con "{tema}" en particular.
        """

        with st.spinner("El agente está preparando la explicación..."):
            try:
                agente = crear_agente_tutor()
                respuesta = agente.run(mensaje)

                st.subheader("Respuesta del agente")
                st.markdown(respuesta.content)

            except Exception as error:
                st.error(
                    "No fue posible conectar con LM Studio.\n\n"
                    f"Detalle: {error}"
                )

st.divider()

st.caption(
    "Proyecto educativo con Python, Agno, Streamlit y LM Studio."
)
