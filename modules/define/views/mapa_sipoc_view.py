import streamlit as st
import pandas as pd


def mapa_sipoc_view():
    st.write(
        "O SIPOC é o mapeamento macro do processo, que garante que a equipe se ambiente ao trabalho que envolve o resultado a melhorar. É importante, por exemplo, para quando os belts do projeto não são da área de escopo.")

    col1_sipoc, col2_sipoc = st.columns(2)

    with col1_sipoc:
        st.text_input("__Início__")

    with col2_sipoc:
        st.text_input("__Fim__")

    tabela_sipoc = {
        "Fornecedores": [" ", " ", " ", " ", " ", " ",],
        "Entradas": [" ", " ", " ", " ", " ", " ",],
        "Processos": [" ", " ", " ", " ", " ", " ",],
        "Saídas": [" ", " ", " ", " ", " ", " ",],
        "Clientes": [" ", " ", " ", " ", " ", " "]
    }

    df_tabela_sipoc = pd.DataFrame(tabela_sipoc)
    tabela_editada_sipoc = st.data_editor(
        df_tabela_sipoc,
        hide_index=True,
        width=1375
    )
