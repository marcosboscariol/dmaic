import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from modules.define.views.analise_viabilidade_view import analise_viabilidade_view
from modules.define.views.project_charter_view import project_charter_view
from modules.define.views.mapa_sipoc_view import mapa_sipoc_view
from modules.define.views.voc_vob_view import voc_vob_view
from modules.define.views.mapa_indicadores_view import mapa_indicadores_view
from modules.define.views.baseline_metas_view import baseline_metas_view
from modules.define.views.gant_view import gant_view
from modules.define.views.mapa_mental_view import mapa_mental_view

selecionar_projeto = st.sidebar.selectbox(
    'Selecione o Projeto', ['Projeto 1', 'Projeto 2'])

st.markdown(f'Projeto selecionado: __{selecionar_projeto}__')

total_itens_concluidos = 0
total_itens_se_aplica = 0

st.session_state_analise_viabilidade_concluido = False
st.session_state_analise_viabilidade_se_aplica = True

st.session_state_project_charter_concluido = False
st.session_state_project_charter_se_aplica = True

st.session_state_sipoc_concluido = False
st.session_state_sipoc_se_aplica = True

st.session_state_vocvob_concluido = False
st.session_state_vocvob_se_aplica = True

st.session_state_mapa_indicadores_concluido = False
st.session_state_mapa_indicadores_se_aplica = True

st.session_state_baseline_concluido = False
st.session_state_baseline_se_aplica = True

st.session_state_gantt_concluido = False
st.session_state_gantt_se_aplica = True

st.session_state_mapa_mental_concluido = False
st.session_state_mapa_mental_se_aplica = True

st.title("Define")

col1av, col2av = st.columns([22, 1])

with col1av:
    with st.expander("__Análise de Viabilidade__"):
        ativo_inativo_analise_viabilidade = st.checkbox(
            'Ativo', value=True, key='ativo_analise_viabilidade')
        if ativo_inativo_analise_viabilidade:
            total_itens_se_aplica = total_itens_se_aplica + 1
            analise_viabilidade_view()
            concluido_analise_viabilidade = st.checkbox(
                'Concluido', key='concluido_analise_viabilidade')
            if concluido_analise_viabilidade:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_analise_viabilidade_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_analise_viabilidade_se_aplica = False

with col2av:
    if st.session_state_analise_viabilidade_concluido:
        st.success('✅')
    elif not st.session_state_analise_viabilidade_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')


col1pc, col2pc = st.columns([22, 1])


with col1pc:
    with st.expander("__Project Charter__"):
        ativo_inativo_project_charter = st.checkbox(
            'Ativo', value=True, key='ativo_project_charter')
        if ativo_inativo_project_charter:
            total_itens_se_aplica = total_itens_se_aplica + 1
            project_charter_view()
            concluido_project_charter = st.checkbox(
                'Concluido', key='concluido_project_charter')
            if concluido_project_charter:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_project_charter_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_project_charter_se_aplica = False


with col2pc:
    if st.session_state_project_charter_concluido:
        st.success('✅')
    elif not st.session_state_project_charter_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')

# Mapa SIPOC

col1sp, col2sp = st.columns([22, 1])

with col1sp:
    with st.expander("__Mapa SIPOC__"):
        ativo_inativo_sipoc = st.checkbox(
            'Ativo', value=True, key='ativo_sipoc')
        if ativo_inativo_sipoc:
            total_itens_se_aplica = total_itens_se_aplica + 1
            mapa_sipoc_view()
            concluido_sipoc = st.checkbox(
                'Concluido', key='concluido_sipoc')
            if concluido_sipoc:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_sipoc_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_sipoc_se_aplica = False


with col2sp:
    if st.session_state_sipoc_concluido:
        st.success('✅')
    elif not st.session_state_sipoc_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')

# VOC/VOB
col1vc, col2vc = st.columns([22, 1])

with col1vc:
    with st.expander("__VOC/VOB__"):
        ativo_inativo_vocvob = st.checkbox(
            'Ativo', value=True, key='ativo_vocvob')
        if ativo_inativo_vocvob:
            total_itens_se_aplica = total_itens_se_aplica + 1
            voc_vob_view()
            concluido_vocvob = st.checkbox(
                'Concluido', key='concluido_vocvob')
            if concluido_vocvob:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_vocvob_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_vocvob_se_aplica = False


with col2vc:
    if st.session_state_vocvob_concluido:
        st.success('✅')
    elif not st.session_state_vocvob_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')

# Mapa de Indicadores
col1mi, col2mi = st.columns([22, 1])

with col1mi:
    with st.expander("__Mapa de Indicadores__"):
        ativo_inativo_mapa_indicadores = st.checkbox(
            'Ativo', value=True, key='ativo_mapa_indicadores')
        if ativo_inativo_mapa_indicadores:
            total_itens_se_aplica = total_itens_se_aplica + 1
            mapa_indicadores_view()
            concluido_mapa_indicadores = st.checkbox(
                'Concluido', key='concluido_mapa_indicadores')
            if concluido_mapa_indicadores:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_mapa_indicadores_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_mapa_indicadores_se_aplica = False


with col2mi:
    if st.session_state_mapa_indicadores_concluido:
        st.success('✅')
    elif not st.session_state_mapa_indicadores_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')

# Baseline e Meta
col1bl, col2bl = st.columns([22, 1])

with col1bl:
    with st.expander("__Baseline e Meta__"):
        ativo_inativo_baseline = st.checkbox(
            'Ativo', value=True, key='ativo_baseline')
        if ativo_inativo_baseline:
            total_itens_se_aplica = total_itens_se_aplica + 1
            baseline_metas_view()
            concluido_baseline = st.checkbox(
                'Concluido', key='concluido_baseline')
            if concluido_baseline:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_baseline_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_baseline_se_aplica = False


with col2bl:
    if st.session_state_baseline_concluido:
        st.success('✅')
    elif not st.session_state_baseline_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')


# Gantt
col1gt, col2gt = st.columns([22, 1])

with col1gt:
    with st.expander("__Gantt__"):
        ativo_inativo_gantt = st.checkbox(
            'Ativo', value=True, key='ativo_gantt')
        if ativo_inativo_gantt:
            total_itens_se_aplica = total_itens_se_aplica + 1
            gant_view()
            concluido_gantt = st.checkbox(
                'Concluido', key='concluido_gantt')
            if concluido_gantt:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_gantt_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_gantt_se_aplica = False


with col2gt:
    if st.session_state_gantt_concluido:
        st.success('✅')
    elif not st.session_state_gantt_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')

# Mapa Mental
col1mm, col2mm = st.columns([22, 1])

with col1mm:
    with st.expander("__Mapa Mental__"):
        ativo_inativo_mapa_mental = st.checkbox(
            'Ativo', value=True, key='ativo_mapa_mental')
        if ativo_inativo_mapa_mental:
            total_itens_se_aplica = total_itens_se_aplica + 1
            mapa_mental_view()
            concluido_mapa_mental = st.checkbox(
                'Concluido', key='concluido_mapa_mental')
            if concluido_mapa_mental:
                total_itens_concluidos = total_itens_concluidos + 1
                st.success(f'Módulo finalizado {datetime.date.today()}')
                st.session_state_mapa_mental_concluido = True
        else:
            st.warning('Módulo Inativo')
            st.session_state_mapa_mental_se_aplica = False


with col2mm:
    if st.session_state_mapa_mental_concluido:
        st.success('✅')
    elif not st.session_state_mapa_mental_se_aplica:
        st.warning('🟡')
    else:
        st.info('🔵')


# Criando um DataFrame com esses valores
data = pd.DataFrame({
    'Categoria': ['Itens que se aplicam'],  # Nome da categoria para o eixo Y
    'Valores': [total_itens_concluidos],    # Valor concluído para o eixo X
    # Rótulo personalizado
    'Label': [f"{total_itens_concluidos}/{total_itens_se_aplica}"]
})

# Criando o gráfico de barras horizontais
fig = px.bar(
    data_frame=data,
    x='Valores',                # eixo X
    y='Categoria',              # eixo Y
    # Limite do eixo X com base no total_itens_se_aplica
    range_x=[0, (total_itens_se_aplica + 1)],
    text='Label',               # Adiciona o rótulo na barra
    labels={'Categoria': 'Categoria',
            'Valores': 'Itens Concluídos'},
    title="Progresso do Total de Itens",
    orientation='h',            # Define barras horizontais
    color_discrete_sequence=['#81C784']  # Cor suave das barras
)

# Atualizando a aparência do texto no gráfico
fig.update_traces(textposition='inside', textfont_size=14,
                  textfont_color='white')

# Ajustando layout
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
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        zerolinecolor='black',
        tickmode='array',  # Define os ticks como uma lista de valores
        # Inclui todos os valores até o máximo
        tickvals=list(range(total_itens_se_aplica + 1)),
        range=[0, total_itens_se_aplica + 1],  # Garante o range do eixo
        tickfont=dict(size=14)
    ),
    yaxis=dict(tickfont=dict(size=14))
)

# Renderizar o gráfico de progresso das etapas
st.plotly_chart(fig, use_container_width=True)
