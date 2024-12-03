import streamlit as st


st.set_page_config(layout="wide")

intro_page = st.Page(
    page='modules/intro/intro_page.py',
    title="Introdução",
    icon='📚'
)

home_page = st.Page(
    page='modules/home/home_page.py',
    title="Home",
    icon='🏠'
)


login_page = st.Page(
    page='modules/login/login_page.py',
    title="Login",
    icon='🔑'
)

define_page = st.Page(
    page='modules/define/define_page.py',
    title='Define',
    icon="📖"
)

measure_page = st.Page(
    page="modules/measure/measure_page.py",
    title='Measure',
    icon="🧮"
)

analyze_page = st.Page(
    page='modules/analyze/analyze_page.py',
    title='Analyze',
    icon="🔍"
)

improve_page = st.Page(
    page='modules/improve/improve_page.py',
    title='Improve',
    icon="📈"
)

control_page = st.Page(
    page='modules/control/control_page.py',
    title='Control',
    icon="📊"
)

indicadores_page = st.Page(
    page='modules/indicadores/indicadores_page.py',
    title='Indicadores',
    icon="📈"
)


if 'username' not in st.session_state:
    st.session_state.username = None

if 'password' not in st.session_state:
    st.session_state.password = None


def main():
    modules = {
        'Login': [login_page],
        'Introdução': [intro_page],
        'Home': [home_page],
        'DMAIC': [define_page, measure_page, improve_page, analyze_page, control_page],
        'Indicadores': [indicadores_page]
    }

    if st.session_state.username != None:
        modules.pop('Login')
    else:
        modules.pop('DMAIC')
        modules.pop('Indicadores')
        modules.pop('Home')
        modules.pop('Introdução')

    pg = st.navigation(modules)
    pg.run()


if __name__ == '__main__':
    main()
