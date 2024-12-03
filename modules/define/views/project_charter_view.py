import streamlit as st
import pandas as pd

st.session_state_importancia = False


def project_charter_view():
    st.write(
        "O Project Charter é o documento que lança o projeto e serve como resumo da iniciativa.")
    st.write("Além de preenchido, deve ser validado pelo Champion em sua totalidade.")
    st.write("Dentre as informações, as mais importantes são: Meta, equipe do projeto, prazos, descrição do problema e escopo.")

    st.write("#### Título do Projeto: ")

    titulo_projeto = st.text_input("_Informe o título do projeto_")

    lider_projeto = st.text_input("_Informe o lider do projeto_")

    sponsor_projeto = st.text_input("_Informe o sponsor do projeto_")

    master_black_belt_projeto = st.text_input(
        "_Informe o Master Black Belt do projeto_")

    champion_projeto = st.text_input("_Informe o championo do projeto_")

    st.write("#### Importância do Processo")

    importancia_do_processo = st.text_area(
        "Ligação com a Estratégia", help="_Objetivo estratégico e meta específica à qual o projeto está ligado._ __Exemplo:__ Objetivo: Aumentar a Receita Operacional Líquida até 2020. Meta: Aumentar 2 pontos percentuais.]")
    st.session_state_importancia = importancia_do_processo
    st.write("#### Problema do processo")

    problema_do_processo = st.text_area(
        "Descrição do problema / oportunidade:", help="_Detalhamento das análises que levaram à identificação da oportunidade._ __Exemplo:__ Nos anos de 2014, 2015 e 2016 o comportamento da margem de resultado no Néctar em percentual foram, -3,9%, -10,9% e -13,2% e em Alimento a base de soja foram 1,6%, -12,0% e -5%. Em 2016 o orçamento foi de  22.046.482 Milhões de Litros de Bebidas (sendo  12.420.720 em Néctar e 9.625.762 em ABSO) com uma meta de resultado em 0,1% (1,6% no Néctar e -2% no ABSO) , porém foi realizado um faturamento de 16.834.644 Milhões (sendo 9.997.509 em Néctar e 6.837.135 no ABSO)  de litros com um resultado líquido de -9,8% (sendo -13,2% no Néctar e -5% no ABSO)  (R$ -3.962.998), ficando o resultado 98% fora do objetivo. Para o orçamento de 2017 a meta de faturamento é de 19.912.906 litros (11.412.906 em Néctar e 8.500.000 em ABSO), tendo como meta 0,11% (-2,83% no Néctar e 4,27% no ABSO) de resultados nas bebidas, com valor aproximado de resultado sendo R$ 57.783,00. (sendo R$ - 885.935 em Néctar e R$ 943.713 no ABSO)")

    st.write("#### Detalhamento do Projeto")

    meta = st.text_area(
        "Meta:", help="_Meta específica do projeto, em indicador técnico e em dinheiro._ __Exemplo:__ Recuperar a rentabilidade de bebidas de -9,78% para -5% (R$ 5 milhões de retorno)")

    meta = st.text_area(
        "Escopo e fronteiras do processo:", help="_Definir o que é e não é escopo do projeto._ __Exemplo:__ Atuar na negociação do pedido (preço médio), no acompanhamento dos descontos concedidos e no controle da compra de insumos (polpa), mas não na industrialização do produto acabado.")

    st.write("##### Equipe do Projeto")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("Black Belts")
    with col2:
        st.text_input("Green Belts")
    with col3:
        st.text_input("Yellow Belts e Outros")
    with col4:
        st.text_input("Especialistas")

    st.write("##### Cronograma Macro")

    tabela_cronograma_macro = {
        "Etapa": ["Definir",
                  "Medir",
                  "Analisar",
                  "Implementar",
                  "Controlar",
                  "Controle e Captura"],
        "Início Previsto": ["", "", "", "", "", ""],
        "Término Previsto": ["", "", "", "", "", ""],
        "Início Real": ["", "", "", "", "", ""],
        "Término Real": ["", "", "", "", "", ""]
    }

    df_tabela_cronograma_macro = pd.DataFrame(tabela_cronograma_macro)
    tabela_editada_cronograma_macro = st.data_editor(
        df_tabela_cronograma_macro,
        hide_index=True,
        width=1375
    )

    st.write("#### Indicadores do Projeto")

    if 'values' not in st.session_state:
        st.session_state['values'] = []

    # Input de texto para adicionar valores
    new_value = st.text_input("Adicione um valor:")

    # Botão para adicionar o valor à lista
    if st.button("Adicionar Valor"):
        if new_value:
            st.session_state['values'].append(new_value)
            st.success(f"Valor '{new_value}' adicionado!")
        else:
            st.warning("Por favor, insira um valor antes de adicionar.")

    # Exibe a lista de valores adicionados
    st.write("Indicadores cadastrados:")
    if st.session_state['values']:
        for idx, value in enumerate(st.session_state['values']):
            st.write(f"__{value}__")
    else:
        st.write("Nenhum valor adicionado ainda.")

    st.text(st.session_state_importancia)
