import streamlit as st


def mapa_mental_view():
    st.write("O Mapa Mental é utilizado para organizar as ideias e as pendências que surgem ao longo de cada etapa do projeto. Pode ser construído como a equipe quiser, desde que feito em grupo e que represente as informações de forma lógica.")

    imagem_mapa_mental = st.file_uploader(
        "Carregue sua imagem do Mapa Mental")

    if imagem_mapa_mental:
        st.image(imagem_mapa_mental)
