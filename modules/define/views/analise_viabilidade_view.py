import streamlit as st
import pandas as pd


def analise_viabilidade_view():
    st.write("Para avaliar se um projeto é mesmo LSS, preencha a tabela abaixo de acordo com o grau de concordância.")
    st.write("Os primeiros 3 critérios são excludentes: se seu projeto não se encaixar nos três, o direcionamento deve ser revisto;")
    st.write("Os outros 4 critérios são decidisivos e deveriam ser atendidos também, mas não impedem o projeto de acontecer. São obstáculos críticos que devem ser superados.")

    tabela_analise_viabilidade = {
        "Item": ["O projeto está alinhado com a estratégia da empresa?",
                 "Está envolvido um ganho de, no mínimo, 200 a 300 mil reais?",
                 "O Champion e as lideranças apoiam o projeto?",
                 "Há probabilidade de sucesso favorável à equipe?",
                 "O time possui a senioridade necessária para executar o projeto?",
                 "Há autoridade e autonomia para a execução das melhorias?",
                 "O projeto pode ser finalizado com 4 a 8 meses de execução?"],
        "Grau de Concordância": [0, 0, 0, 0, 0, 0, 0]
    }

    df_tabela_analise_viabilidade = pd.DataFrame(tabela_analise_viabilidade)
    tabela_editada = st.data_editor(
        df_tabela_analise_viabilidade,
        column_config={
            "Grau de Concordância": st.column_config.SelectboxColumn(
                options=[1, 2, 3, 4, 5]
            )
        },
        hide_index=True,
    )

    # Acessando o valor específico da primeira linha e coluna "Nota"
    grau_concordancia_1 = tabela_editada.at[0, 'Grau de Concordância']
    grau_concordancia_2 = tabela_editada.at[1, 'Grau de Concordância']
    grau_concordancia_3 = tabela_editada.at[2, 'Grau de Concordância']
    grau_concordancia_4 = tabela_editada.at[3, 'Grau de Concordância']
    grau_concordancia_5 = tabela_editada.at[4, 'Grau de Concordância']
    grau_concordancia_6 = tabela_editada.at[5, 'Grau de Concordância']
    grau_concordancia_7 = tabela_editada.at[6, 'Grau de Concordância']

    soma_grau_concordancia = (grau_concordancia_1 + grau_concordancia_2 + grau_concordancia_3 +
                              grau_concordancia_4 + grau_concordancia_5 + grau_concordancia_6 + grau_concordancia_7)

    grau_concordancia_divisor_1 = 0
    if grau_concordancia_1 != 0:
        grau_concordancia_divisor_1 = 1

    grau_concordancia_divisor_2 = 0
    if grau_concordancia_2 != 0:
        grau_concordancia_divisor_2 = 1

    grau_concordancia_divisor_3 = 0
    if grau_concordancia_3 != 0:
        grau_concordancia_divisor_3 = 1

    grau_concordancia_divisor_4 = 0
    if grau_concordancia_4 != 0:
        grau_concordancia_divisor_4 = 1

    grau_concordancia_divisor_5 = 0
    if grau_concordancia_5 != 0:
        grau_concordancia_divisor_5 = 1

    grau_concordancia_divisor_6 = 0
    if grau_concordancia_6 != 0:
        grau_concordancia_divisor_6 = 1

    grau_concordancia_divisor_7 = 0
    if grau_concordancia_7 != 0:
        grau_concordancia_divisor_7 = 1

    soma_grau_concordancia_divisor = (grau_concordancia_divisor_1 + grau_concordancia_divisor_2 + grau_concordancia_divisor_3 +
                                      grau_concordancia_divisor_4 + grau_concordancia_divisor_5 + grau_concordancia_divisor_6 + grau_concordancia_divisor_7)

    if grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0 and grau_concordancia_1 == 0:
        st.write("Informe os valores para realizar a análise de viabilidade.")
    elif grau_concordancia_1 < 5 or grau_concordancia_2 < 5 or grau_concordancia_3 < 5:
        st.error(
            "O projeto pouco se caracteriza como Lean Seis Sigma. O escopo deve ser revisto com o Champion antes do início.")
    elif soma_grau_concordancia/soma_grau_concordancia_divisor < 4:
        st.warning(
            "O projeto pode ser considerado Lean Seis Sigma, mas pode ser ajustado para garantir maior chance de sucesso.")
    else:
        st.success("O projeto atende plenamente aos critérios Lean Seis Sigma.")
