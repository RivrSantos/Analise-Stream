import streamlit as st
import pandas as pd

motos_rev = pd.read_csv('table_moto.csv')
servico = pd.read_csv('table_clientes.csv')
anos = pd.read_excel('Registro_ano.xlsx')
regi = pd.read_csv('realatorio_moto.csv')

st.logo('carmo.png')


def table():
    st.header("Tabelas de Dados", divider=True)
    option = st.selectbox(
        "",
        ("🛠 SERVIÇO", "🏍 MOTOS", "✔ ANO-FABRICAÇAO", "🗓 REGISTRO-BRUTO"),
        index=None,
        placeholder=" Buscar tabelas...")

    if option == "🏍 MOTOS":
        st.dataframe(motos_rev, hide_index=True)
    elif option == "🛠 SERVIÇO":
        st.dataframe(servico, hide_index=True)
    elif option == '✔ ANO-FABRICAÇAO':
        st.dataframe(anos, hide_index=True)
    elif option == '🗓 REGISTRO-BRUTO':
        st.dataframe(regi, hide_index=True, width=800, height=700)
        st.info('💡 . Os serviços podem variar de acordo com a demanda')


table()

st.sidebar.metric(label="ATENDIMENTOS", value=42,
                  delta='3.8%', delta_color='normal')
st.sidebar.divider()
st.sidebar.metric(label="REVISOES PREÇO FIXO", value=21,
                  delta='2.5%', delta_color='normal')
st.sidebar.divider()
st.sidebar.metric(label="SERVIÇOS FORA DE GARANTIA",
                  value=18, delta='3.8%', delta_color='normal')
st.sidebar.divider()
st.sidebar.metric(label="OUTROS", value=3, delta='-1.3%', delta_color='normal')
st.sidebar.divider()

st.sidebar.markdown('AVALIAR CONTEUDO')
avaliar = st.sidebar.feedback('thumbs')
