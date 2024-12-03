import streamlit as st


def mapa_processo_view():
    st.write("Mapeamento de processos é uma ferramenta gerencial que tem como objetivo identificar as informações, o fluxo, as partes envolvidas, capacidades, competências e recursos para atender todos os componentes necessários fazendo com que todas as atividades de uma empresa ou negócio saiam conforme o planejado, com poucas alterações e sem problemas.")

    imagem_mapa_processo = st.file_uploader(
        "Carregue sua imagem do Mapa do Processo")

    if imagem_mapa_processo:
        st.image(imagem_mapa_processo)
