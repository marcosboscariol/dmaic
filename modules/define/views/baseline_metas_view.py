import streamlit as st
import pandas as pd
import plotly.express as px


def baseline_metas_view():
    st.write("O ganho pode ser projetado tanto no indicador do tipo técnico quanto no próprio volume financeiro. É importante projetar o ganho do projeto para entender se o esforço trará a recompensa conforme o esperado.")

    st.write("#### Cálculo de Ganho - Indicador Técnico (Y)")

    col1_baseline_meta, col2_baseline_meta = st.columns(2)

    with col2_baseline_meta:
        st.write("__Dados__")

        # Tópicos iniciais
        topics = ["Baseline", "Benchmarking", "Lacuna", "Ganho", "Meta"]

        # Cria uma tabela inicial com valores 0
        data = pd.DataFrame({"Tópico": topics, "Valor": [0] * len(topics)})

        # Exibe a tabela e permite que o usuário edite os valores
        st.write("Preencha a tabela abaixo:")
        edited_data = st.data_editor(data, hide_index=True)

    with col1_baseline_meta:
        st.write("__Ganho Projetado__")
        # Cria um gráfico de barras responsivo aos valores da tabela
        fig = px.bar(edited_data, x="Tópico", y="Valor")
        st.plotly_chart(fig)
