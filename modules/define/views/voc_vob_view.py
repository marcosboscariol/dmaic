import streamlit as st


def voc_vob_view():
    st.write("A voz do cliente é utilizada para capturar o que seu cliente espera de um determinado processo, ou seja, o que ele considera bom.")
    st.write("Já a VOB é o que o seu processo consegue produzir. Ambos, VOC e VOB andam sempre juntos em um programa de melhoria como o Six Sigma.")
    st.write("Entender a voz dos diferentes clientes e garantir a sua satisfação é essencial para qualquer empresa.")

    st.write("#### Controle da Qualidade Total")

    col1_vocvob, col2_vocvob, col3_vocvob = st.columns(3)

    # Inicializar listas separadas no session_state, se ainda não existirem
    if 'values_col1' not in st.session_state:
        st.session_state['values_col1'] = []

    if 'values_col2' not in st.session_state:
        st.session_state['values_col2'] = []

    if 'values_col3' not in st.session_state:
        st.session_state['values_col3'] = []

    with col1_vocvob:
        new_value_col1_vocvob = st.text_input("__Qualidade (CTQ)__")
        if st.button("Adicionar Valor para Qualidade (CTQ)"):
            if new_value_col1_vocvob:
                st.session_state['values_col1'].append(new_value_col1_vocvob)
                st.success(f"Valor '{new_value_col1_vocvob}' adicionado!")
            else:
                st.warning("Por favor, insira um valor antes de adicionar.")

        # Exibe a lista de valores adicionados
        st.write("Valores cadastrados para Qualidade (CTQ):")
        if st.session_state['values_col1']:
            for idx, value in enumerate(st.session_state['values_col1']):
                st.write(f"__{value}__")
        else:
            st.write("Nenhum valor adicionado ainda.")

    with col2_vocvob:
        new_value_col2_vocvob = st.text_input("__Custo (CTC)__")
        if st.button("Adicionar Valor para Custo (CTC)"):
            if new_value_col2_vocvob:
                st.session_state['values_col2'].append(new_value_col2_vocvob)
                st.success(f"Valor '{new_value_col2_vocvob}' adicionado!")
            else:
                st.warning("Por favor, insira um valor antes de adicionar.")

        # Exibe a lista de valores adicionados
        st.write("Valores cadastrados para Custo (CTC):")
        if st.session_state['values_col2']:
            for idx, value in enumerate(st.session_state['values_col2']):
                st.write(f"__{value}__")
        else:
            st.write("Nenhum valor adicionado ainda.")

    with col3_vocvob:

        new_value_col3_vocvob = st.text_input("__Entrega (CTD)__")
        if st.button("Adicionar Valor para Entrega (CTD)"):
            if new_value_col3_vocvob:
                st.session_state['values_col3'].append(new_value_col3_vocvob)
                st.success(f"Valor '{new_value_col3_vocvob}' adicionado!")
            else:
                st.warning("Por favor, insira um valor antes de adicionar.")

        # Exibe a lista de valores adicionados
        st.write("Valores cadastrados para Entrega (CTD):")
        if st.session_state['values_col3']:
            for idx, value in enumerate(st.session_state['values_col3']):
                st.write(f"__{value}__")
        else:
            st.write("Nenhum valor adicionado ainda.")
