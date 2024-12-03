import streamlit as st

# Definindo o estilo uma vez para aplicar a todos os textos
st.markdown("""
    <style>
    /* Estilo para a página */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f7f7f7;
        color: #333;
    }
    
    /* Estilo dos títulos */
    h1 {
        color: #3E4A59;
        text-align: center;
        font-size: 40px;
        margin-bottom: 10px;
    }

    h3 {
        color: #2F4F4F;
        font-size: 24px;
        margin-bottom: 5px;
    }
    
    /* Estilo para os benefícios em formato de cards */
    .benefit-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;  /* Diminui o padding */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;  /* Reduz o espaçamento entre os cards */
        height: 130px;  /* Reduz a altura do card */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .benefit-title {
        font-size: 20px;  /* Tamanho da fonte do título (restaurado) */
        font-weight: bold;
        color: #4CAF50;
        margin-bottom: 5px;  /* Menos espaço abaixo do título */
    }

    .benefit-text {
        font-size: 16px;  /* Tamanho da fonte do texto (restaurado) */
        color: #333;
        line-height: 1.4;  /* Ajusta o espaçamento entre linhas */
    }

    /* Estilo para as colunas (para os cards) */
    .stColumn {
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title('Benefícios da Sistematização da Metodologia DMAIC via Streamlit')

# Títulos e textos com o estilo aplicado
benefits = [
    ("Centralização e Organização",
     "Streamlit oferece uma interface única, evitando os problemas de descentralização e inconsistências do Excel."),
    ("Acesso Controlado e Colaborativo",
     "Controle de acessos e privilégios por autenticação, superando limitações de compartilhamento do Excel."),
    ("Integração com IA",
     "Possibilidade de incluir inteligência artificial diretamente no sistema, algo inviável no Excel."),
    ("Automatização de Processos",
     "Redução de trabalho manual com gráficos e relatórios automatizados em tempo real."),
    ("Segurança de Dados",
     "Dados armazenados de forma segura em servidores com controle de acesso."),
    ("Relatórios Dinâmicos",
     "Relatórios e gráficos atualizados automaticamente, refletindo mudanças em tempo real."),
    ("Melhor Visibilidade para Gestores",
     "Painéis customizados permitem monitorar KPIs e progresso de maneira eficaz."),
    ("Personalização",
     "Fluxos e funcionalidades podem ser ajustados às necessidades específicas do projeto DMAIC.")
]

# Organizando em 4 colunas, dividindo os benefícios em blocos
cols = st.columns(4)

# Exibindo os benefícios dentro de cada coluna
for i, (title, text) in enumerate(benefits):
    with cols[i % 4]:  # Organiza as colunas em loop
        st.markdown(
            f'<div class="benefit-card"><div class="benefit-title">{title}</div><div class="benefit-text">{text}</div></div>', unsafe_allow_html=True)
