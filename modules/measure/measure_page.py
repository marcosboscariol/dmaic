import streamlit as st
import cohere
from modules.measure.views.mapa_processo_view import mapa_processo_view
from modules.measure.views.ishikawa_view import ishikawa_view


selecionar_projeto = st.sidebar.selectbox(
    'Selecione o Projeto', ['Projeto 1', 'Projeto 2'])

st.markdown(f'Projeto selecionado: __{selecionar_projeto}__')


st.title("Measure")

st.text(st.session_state_importancia)

with st.expander('__Mapa do Processo__'):
    mapa_processo_view()

with st.expander('__Diagrama de Ishikawa__'):
    ishikawa_view()

with st.expander('__Matriz Causa e Efeito__'):
    st.subheader('Matriz Causa e Efeito')


with st.expander('__Ánalise da Medição__'):
    st.subheader('Ánalise da Medição')


with st.expander('__Coleta de Dados__'):
    st.subheader('Coelta de Dados')


with st.expander('__Capacidade do Processo__'):
    st.subheader('Capacidade do Processo')


with st.expander('__Mapa Mental__'):
    st.subheader('Mapa Mental')
