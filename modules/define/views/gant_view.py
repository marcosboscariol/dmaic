import streamlit as st
import pandas as pd
import plotly.express as px


def gant_view():
    st.write("O diagrama de Gantt é um gráfico usado para ilustrar o avanço das diferentes etapas de um projeto. Os intervalos de tempo representando o início e fim de cada fase aparecem como barras coloridas sobre o eixo horizontal do gráfico.")

    # Definindo os dados da tabela
    tasks = [
        "Elaborar o Project Charter", "Definir a equipe e a dedicação", "Estabelecer a meta preliminar",
        "Validar com o Champion", "Desenhar o Mapa SIPOC", "Preencher e analisar VOC/VOB",
        "Desenhar a Árvore de Indicadores", "Priorizar os principais Ys", "Validar com o Champion",
        "Estabelecer a meta dos Ys", "Calcular meta no indicador", "Calcular ganho previsto",
        "Validar cálculos com o financeiro", "Preencher o cronograma", "Desenhar Mapa Mental",
        "Aplicar Análise GRIP: Definir", "Validar etapa com Champion", "Mapear o processo",
        "Listar Ganhos Rápidos", "Validar com o Champion", "Levantar causas (X): Ishikawa",
        "Priorizar causas: Matriz Causa-Efeito", "Analisar o Sistema de Medição", "Coletar dados do processo",
        "Calcular a Capacidade", "Desenhar Mapa Mental", "Aplicar Análise GRIP: Medir",
        "Validar etapa com Champion", "Levantar causas-raíz", "Elaborar o FMEA", "Preencher Modos de Falha, Efeitos, Causas e Controles",
        "Atribuir notas e priorizar", "Fazer 5 Porquês com as causas do FMEA", "Testar Hipóteses levantadas",
        "Testar influência dos X nos Y: Regressão", "Listar causas-raíz comprovadas", "Desenhar Mapa Futuro",
        "Listar Ganhos Rápidos", "Desenhar Mapa Mental", "Aplicar Análise GRIP: Analisar", "Validar etapa com Champion",
        "Gerar soluções: brainstorm", "Listar soluções", "Priorizar soluções", "Aplicar Análise GRIP: Implementar",
        "Validar com o Champion", "Criar o Plano de Ação", "Desenhar Mapa Mental", "Monitorar o Y e tratar desvios",
        "Remover causas especiais", "Calcular ganho real e previsto", "Padronizar o Processo",
        "Criar CEPs, OCAP, PTPs e POPs", "Treinar a operação", "Calcular a nova Capacidade",
        "Aplicar Análise GRIP: Controlar", "Validar etapa com Champion"
    ]

    # Cria um DataFrame com os dados
    df = pd.DataFrame({
        "Tarefa": tasks,
        "Etapa DMAIC": ["" for _ in tasks],
        "Responsável": ["" for _ in tasks],
        "Data início Previsto": ["" for _ in tasks],
        "Data término Previsto": ["" for _ in tasks],
        "Data início Realizado": ["" for _ in tasks],
        "Data término Realizado": ["" for _ in tasks],
        "Status": ["" for _ in tasks]
    })

    # Exibe a tabela para que o usuário possa preencher os dados
    st.write("Preencha a tabela abaixo:")
    edited_df = st.data_editor(df)

    # Cria um gráfico de Gantt com base nos dados preenchidos
    # (Assumindo que o usuário irá preencher as datas e status)
    if not edited_df["Data início Previsto"].isnull().all() and not edited_df["Data término Previsto"].isnull().all():
        fig = px.timeline(
            edited_df,
            x_start="Data início Previsto",
            x_end="Data término Previsto",
            y="Tarefa",
            color="Status",
            title="Gantt Chart"
        )
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig)
    else:
        st.write("Preencha as datas para visualizar o gráfico de Gantt.")
