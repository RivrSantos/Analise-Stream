from pages import Introduçao, Graficos, Tabelas, Mapas
import pandas as pd
import streamlit as st
import openpyxl

st.logo('carmo.png')
st.header('Apresentaçao', divider=True)
st.markdown('''Nos dias de hoje, a análise de dados é um pilar fundamental para o sucesso empresarial. A capacidade de coletar, processar e interpretar informações tornou-se um ativo vital para as empresas que desejam se manter competitivas e inovadoras. ''')
st.image('banco-de-dados.jpg')
st.divider()
st.markdown('''Adotar uma cultura de dados é igualmente importante. Promover a conscientização sobre a análise de dados em toda a organização e incentivar a colaboração interdepartamental é crucial para o sucesso a longo prazo. Com uma cultura de dados sólida, as empresas podem garantir que a análise seja usada de maneira eficaz e integrada em suas operações.''')
st.divider()
st.markdown('''Em resumo, a análise de dados é um pilar essencial para o sucesso dos negócios modernos. Ela melhora a tomada de decisões, aumenta a eficiência operacional e revela oportunidades de crescimento. Se você deseja que sua empresa prospere e se mantenha competitiva, investir em análise de dados é um passo essencial.''')

# páginas
paginas = {
    "Introdução": Introduçao,
    "Gráficos": Graficos,
    "Mapas": Mapas,
    "Tabelas": Tabelas
}

# st.sidebar.subheader('Relatorio Parcial')
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

