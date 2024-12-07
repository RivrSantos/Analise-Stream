import streamlit as st
import pandas as pd

anos = pd.read_excel('Registro_ano.xlsx')

st.logo('carmo.png')
preco_f = pd.DataFrame({'MES': ['01. Janeiro', '02. Fevereiro', '03. Março', '04. Abril', '05. Maio', '06. Junho', '07. Julho', '08. Agosto', '09. Setembro', '10. Outubro', '11. Novembro'],
                        'QTD REVISOES': [14, 17, 13, 11, 20, 9, 19, 12, 16, 18, 21]}).reset_index()


def grafics():
    st.header("Gráficos", divider=True)
    st.subheader('REGISTRO DE PASSAGEM POR ANO/MODELO')
    st.markdown(' O gráfico apresenta analise impactante em relação a retenção dos clientes que seguem o plano de manutenção  PREÇO FIXO oferecido pela YAMAHA Motor do Brasil. E importante ressaltar que houve aumento de 2,5% em relação ao mês anterior')
    st.bar_chart(anos)
    st.info('💡 . Para mais informações acesse www.yamaha-motor.com')
    st.subheader('REGISTRO DE REVISOES')
    st.markdown(
        ' O gráfico abaixo representa a evolução do programa de Revisão Preço Fixo')
    st.line_chart(preco_f)

grafics()

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

st.subheader('Conclusão')
st.markdown('A analise apresenta resultados positivos em relação ao mês anterior. E importante lembrar que essa analise foi feita com base no fluxo de trabalho de apenas um dos colaboradores do setor de assistência técnica.')

st.sidebar.markdown('AVALIAR CONTEUDO')
avaliar = st.sidebar.feedback('thumbs')
