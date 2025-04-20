import streamlit as st

st.title("Laboratorio Virtual")
#st.components.v1.iframe("https://juancarlosperezdelgado.github.io/Imagenes/index.html", width=1000, height=1000)


st.write(f"""
        <div style="width: 1000; height: 1000px;">
            <iframe src="https://juancarlosperezdelgado.github.io/Imagenes/index.html" style="border: none;"></iframe>
        </div>
        """,unsafe_allow_html=True)

