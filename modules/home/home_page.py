import streamlit as st
import plotly.express as px
import pandas as pd

# Título da página
st.title('Home')

# Saudação com o nome do usuário
if "username" not in st.session_state:
    st.session_state.username = "Usuário"  # Valor padrão para teste
st.markdown(f'### Olá {st.session_state.username}!')

# Definir os botões ou opções de navegação
opcao_selecionada = st.radio(
    "Escolha uma opção",
    ['Detalhes de Projetos', 'Cadastrar Novo Projeto'],
    horizontal=True  # Exibir os botões na horizontal
)

# Lógica para cada opção selecionada
if opcao_selecionada == 'Detalhes de Projetos':
    # Dropdown para seleção de projeto
    projeto_selecionado = st.selectbox(
        'Selecione um Projeto', ['', 'Projeto 1', 'Projeto 2'])

    # Lógica para o Projeto 1
    if projeto_selecionado == 'Projeto 1':
        st.markdown('## Projeto 1')

        st.markdown('### Resumo')

        st.text_area(
            '', value='O Projeto 1 visa aumentar em X% o faturamento da área Y, melhorando os processos da área Z')

        st.markdown('### Termômetro')

        # Dados do gráfico de Progresso das Etapas
        etapas_totais = 45
        etapas_concluidas = 25

        # Criar DataFrame para o gráfico de progresso das etapas
        data = pd.DataFrame({
            'Categoria': ['Etapas concluídas'],
            'Valores': [etapas_concluidas]
        })

        # Criar gráfico de barras horizontais com Plotly Express para progresso das etapas
        fig = px.bar(
            data,
            x='Valores',
            y='Categoria',
            orientation='h',
            title='Progresso das Etapas',
            range_x=[0, etapas_totais],  # Limite do eixo x
            color_discrete_sequence=['#81C784']  # Cor suave das barras
        )

        # Adicionar labels de porcentagem no primeiro gráfico
        porcentagem = (etapas_concluidas / etapas_totais) * 100
        fig.update_traces(
            # Formatar a porcentagem com uma casa decimal
            text=f'{porcentagem:.1f}%',
            textposition='inside',  # Colocar o texto dentro da barra
            insidetextanchor='middle',  # Centralizar o texto dentro da barra
            textfont=dict(
                family="Arial, sans-serif",  # Família da fonte
                size=14,  # Tamanho da fonte
                color="black",  # Cor da fonte
                weight='bold'  # Negrito
            )
        )

        # Atualizar o layout do gráfico de progresso das etapas
        fig.update_layout(
            showlegend=False,
            plot_bgcolor='white',
            bargap=0.5,  # Ajusta o espaçamento entre as barras
            autosize=False,
            width=500,  # Ajuste da largura total do gráfico
            height=300,  # Ajuste da altura para o gráfico de barras
            font=dict(
                family="Arial, sans-serif",  # Família da fonte
                size=14,  # Tamanho da fonte
                color="black"  # Cor da fonte
            ),
            xaxis_title=None,  # Remover título do eixo X
            yaxis_title=None,  # Remover título do eixo Y
            xaxis=dict(showgrid=True, gridcolor='lightgray',
                       zerolinecolor='black', tickfont=dict(size=14)),
            yaxis=dict(tickfont=dict(size=14))
        )

        # Renderizar o gráfico de progresso das etapas
        st.plotly_chart(fig, use_container_width=True)

        # Dados do gráfico das fases DMAIC
        dmaic_data = pd.DataFrame({
            'Fase': ['Define', 'Measure', 'Analyze', 'Improve', 'Control'],
            'Total': [8, 9, 6, 11, 9],
            'Concluídas': [8, 6, 0, 0, 0]
        })

        # Calcular a porcentagem de etapas concluídas em relação ao total
        dmaic_data['Porcentagem'] = (
            dmaic_data['Concluídas'] / dmaic_data['Total']) * 100

        # Criar gráfico de barras horizontais para as fases DMAIC
        fig_dmaic = px.bar(
            dmaic_data,
            x='Concluídas',
            y='Fase',
            orientation='h',
            title='Progresso do DMAIC',
            range_x=[0, max(dmaic_data['Total'])],
            color_discrete_sequence=['#81C784'],  # Cor suave das barras
            category_orders={
                'Fase': ['Define', 'Measure', 'Analyze', 'Improve', 'Control']}
        )

        # Adicionar labels de porcentagem nas barras
        fig_dmaic.update_traces(
            text=dmaic_data['Porcentagem'].round(1).astype(str) + '%',
            textposition='inside',  # Colocar o texto dentro da barra
            insidetextanchor='middle',  # Centralizar o texto dentro da barra
            textfont=dict(
                family="Arial, sans-serif",  # Família da fonte
                size=14,  # Tamanho da fonte
                color="black",  # Cor da fonte
                weight='bold'  # Negrito
            )
        )

        # Atualizar o layout do gráfico DMAIC
        fig_dmaic.update_layout(
            showlegend=False,
            plot_bgcolor='white',
            bargap=0.2,  # Ajusta o espaçamento entre as barras
            autosize=False,
            width=500,  # Ajuste da largura total do gráfico
            height=400,  # Ajuste da altura para o gráfico de barras
            font=dict(
                family="Arial, sans-serif",  # Família da fonte
                size=14,  # Tamanho da fonte
                color="black"  # Cor da fonte
            ),
            xaxis_title=None,  # Remover título do eixo X
            yaxis_title=None,  # Remover título do eixo Y
            xaxis=dict(showgrid=True, gridcolor='lightgray',
                       zerolinecolor='black', tickfont=dict(size=14)),
            yaxis=dict(tickfont=dict(size=14))
        )

        # Renderizar o gráfico de progresso do DMAIC com labels de porcentagem
        st.plotly_chart(fig_dmaic, use_container_width=True)

        if st.button('Acessar DMAIC'):
            st.switch_page('modules/define/define_page.py')

elif opcao_selecionada == 'Cadastrar Novo Projeto':
    st.markdown('## Cadastrar Novo Projeto')
    st.markdown(
        "Aqui você pode cadastrar um novo projeto preenchendo os detalhes abaixo.")
    st.text_input('Nome do Projeto')
    st.text_area('Descrição do Projeto')
    st.button('Cadastrar')
