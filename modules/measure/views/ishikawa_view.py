import streamlit as st
import cohere


# Substitua 'your-cohere-api-key' pela sua chave de API da Cohere
cohere_client = cohere.Client('Sid93B0NN5Vc3luKBnbaD07IYTj93V1HGix5nDEe')


def ishikawa_view():
    pergunta_ishikawa = st.text_area(
        label='Insira uma pergunta sobre o Ishikawa')
    if st.button("Perguntar a IA"):
        try:
            # Gerar sugestão usando a API da Cohere
            response2 = cohere_client.generate(
                model='command-r-plus',  # Utilize um modelo adequado para geração de texto
                prompt=f"Levando em conta que o objetivo do projeto é {st.session_state_importancia}, e essa pergunta está no contexto da ferramenta ishikawa, responda essa pergunta: {pergunta_ishikawa}.",
                # max_tokens=150,  # Limitar o comprimento da resposta
                temperature=0.7
            )

            suggested_solution = response2.generations[0].text
            st.write("Resposta da IA:")
            st.write(suggested_solution)
        except Exception as e:
            st.error(f"Erro ao gerar sugestão: {e}")

    # Input para o problema prioritário
    problema_prioritario = st.text_input("Insira o problema prioritário:")

    # Criando um dicionário para armazenar os valores dos inputs
    input_values = {}

    # Definindo os títulos dos inputs
    input_titles = ["Medição", "Material",
                    "Pessoal", "Máquinas", "Métodos", "Ambiente"]

    # Função para criar e gerenciar inputs dinâmicos

    def dynamic_inputs(title):
        st.subheader(title)

        # Inicializa a lista de valores se não existir
        if title not in st.session_state:
            st.session_state[title] = ['']  # Começa com um campo vazio

        values = st.session_state[title]

        # Mostrar inputs existentes
        for i in range(len(values)):
            values[i] = st.text_input(
                f"{title} {i+1}", value=values[i], key=f"{title}_{i}")

        # Adicionar novo campo de entrada se o botão for clicado
        if st.button(f"Adicionar mais {title}", key=f"add_{title}"):
            values.append('')  # Adiciona um novo campo vazio
            st.session_state[title] = values  # Atualiza o estado da sessão

        # Armazenar os valores atualizados
        input_values[title] = values

    # Dividindo a página em duas seções de 3 colunas cada
    with st.container():
        col1, col2, col3 = st.columns(3)

        # Primeira seção (colunas 1 a 3)
        with col1:
            dynamic_inputs("Medição")

        with col2:
            dynamic_inputs("Material")

        with col3:
            dynamic_inputs("Pessoal")

    with st.container():
        col4, col5, col6 = st.columns(3)

        # Segunda seção (colunas 4 a 6)
        with col4:
            dynamic_inputs("Máquinas")

        with col5:
            dynamic_inputs("Métodos")

        with col6:
            dynamic_inputs("Ambiente")

    # # Exibindo o dicionário com os valores inseridos
    # st.write("Valores inseridos:")
    # st.write(input_values)

    # Unindo todos os valores com seus respectivos títulos para o dropdown
    all_values_with_titles = [
        f"{title}: {value}" for title, values in input_values.items() for value in values if value
    ]

    # Dropdown para selecionar até 5 itens
    selected_items = st.multiselect(
        "Selecione até 5 itens", all_values_with_titles, max_selections=5)

    if selected_items:
        # Dropdown para selecionar um dos 5 valores priorizados
        prioritized_value = st.selectbox(
            "Selecione um dos valores priorizados", selected_items)

        if st.button("Gerar sugestão de solução"):
            try:
                # Gerar sugestão usando a API da Cohere
                response = cohere_client.generate(
                    model='command-r-plus',  # Utilize um modelo adequado para geração de texto
                    prompt=f"Levando em conta que o objetivo do projeto {st.session_state_importancia}, proponha uma solução para o seguinte problema: {prioritized_value}.",
                    # max_tokens=150,  # Limitar o comprimento da resposta
                    temperature=0.7
                )

                suggested_solution = response.generations[0].text
                st.write("Sugestão de solução:")
                st.write(suggested_solution)
            except Exception as e:
                st.error(f"Erro ao gerar sugestão: {e}")
