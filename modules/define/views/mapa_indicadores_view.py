import streamlit as st


def mapa_indicadores_view():
    st.write("A Árvore de Indicadores é utilizada para priorizar o escopo, partindo a partir da meta e desdobrando is itens conforme faça sentido para encontrar problemas menores mas que, quando resulvidos, solucionem um problema maior.")

    imagem_mapa_indicadores = st.file_uploader(
        "Carregue sua imagem do Mapa de Indicadores")

    if imagem_mapa_indicadores:
        st.image(imagem_mapa_indicadores)
