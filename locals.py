import pandas as pd
import streamlit as st


regi= pd.read_csv('realatorio_moto.csv')
anos= pd.read_csv('table_ano.csv')
servico= pd.read_csv('table_clientes.csv')
motos_rev= pd.read_csv('table_moto.csv')

# picture = st.sidebar.camera_input(label='', on_change= False)
# if picture:
#     st.sidebar.image(picture)
st.logo('carmo.png')

# st.sidebar.subheader('SELECIONAR TABELAS')
option = st.sidebar.selectbox(
    "",
    ("🛠 SERVIÇO", "🏍 MOTOS", "✔ ANO-FABRICAÇAO", "🗓 REGISTRO-BRUTO"),
    index=None,
    placeholder=" Buscar tabelas...")

if option == "🏍 MOTOS":
    st.sidebar.dataframe(motos_rev, hide_index= True)
elif option == "🛠 SERVIÇO":
    st.sidebar.dataframe(servico, hide_index= True)
elif option == '✔ ANO-FABRICAÇAO':
    st.sidebar.dataframe(anos, hide_index= True)
elif option == '🗓 REGISTRO-BRUTO':
    st.subheader('DADOS BRUTOS', divider= True)
    st.dataframe(regi, hide_index= True, width= 800, height= 700)
    st.info('Os serviços podem variar de acordo com a demanda')

st.header('ANALISE MENSAL - MONTES CLAROS', divider= True)
st.subheader('DISPERSAO DEMOGRAFICA')
st.markdown(' Diante do atual cenário vale destacar a importância da dispersão geográfica para planejamento de campanhas de marketing e publicidade visando o fortalecendo da marca e a conquista de novos clientes')
st.sidebar.subheader('RELATORIO PARCIAL', divider= True)

localizacao= pd.DataFrame({'LAT': [-16.69641120149624,-17.11615327640339, -16.718440856769977, -16.734519609574676, -16.7294971631257, -16.778051967668613, -16.723197848502167, -16.73931569364286, -16.700298156935425, -16.722586082835015, -16.694218504794108, -16.71735867946006, -16.545894473564132, -16.69715316642467, -22.429669928304584, -20.53436182099107, -16.755251857277372, -16.75174078693976, -16.743163430259067, -16.696285930653286, -16.713269398830658],
            'LONG': [-43.81215144729478, -43.80891260497165, -43.872693433820174, -43.844793491492, -43.83387737614739, -43.868105904982144, -43.86416680021725, -43.86184634731103, -43.85606172905718, -43.8146690184754, -43.836719862657134, -43.817800962656335, -42.51433211089733, -43.83779254360566, -46.58162941450265, -54.67167891834721, -43.86953887799996, -43.889099171376635, -43.87884296080237, -43.851728429057815, -43.85951240313087],
            'CLIENTES': ['sansao-carlos-alves', 'leandro-natalino', 'uasley-costa-rodrigues', 'alfeu-martins-cardoso-jr', 'miaki-luanne-alves-cordeiro', 'elian-cordeiro-santos','victorio-almeida-caratta','guilherme-duarte-moreira','josimarcio-costa-alves','andre-luiz-ferreira-queiroz','eduardo-ferreira-de-franca','claudineia-pereira-costa','vitor-gabriel-silva-vieira','joao-guilherme-santiago-pereira','cleber-lopes','gilson-eder-dias-luz','jeferson-ferreira-oliveira','vitor-junior-lopes-santos','daniela-renata-martins-oliveira','marcela-lima-melo','jose-augusto-oliveira']
                })

st.map(localizacao, latitude= 'LAT', longitude= 'LONG', color='#49CD32', size= 100, use_container_width= True)
st.divider()
st.info('💡 . Os dados são de fonte local, demonstrando a dispersão geográfica de clientes em Montes Claros e região')

st.subheader('REGISTRO DE PASSAGEM POR ANO/MODELO')
st.markdown(' O gráfico apresenta analise impactante em relação a retenção dos clientes que seguem o plano de manutenção  PREÇO FIXO oferecido pela YAMAHA Motor do Brasil. E importante ressaltar que houve aumento de 2,5% em relação ao mês anterior')
st.bar_chart(anos)
st.info('💡 . Para mais informações acesse www.yamaha-motor.com')

preco_f= pd.DataFrame({'MES':['01. Janeiro', '02. Fevereiro', '03. Março', '04. Abril', '05. Maio', '06. Junho', '07. Julho', '08. Agosto', '09. Setembro', '10. Outubro', '11. Novembro'],
'QTD REVISOES':[14, 17, 13, 11, 20, 9, 19, 12, 16, 18, 21]}).reset_index()

st.subheader('REGISTRO DE REVISOES')
st.markdown(' O gráfico abaixo representa a evolução do programa de Revisão Preço Fixo')
st.bar_chart(preco_f, x= 'MES', y= 'QTD REVISOES')

st.subheader('Conclusão')
st.markdown('A analise apresenta resultados positivos em relação ao mês anterior. E importante lembrar que essa analise foi feita com base no fluxo de trabalho de apenas um dos colaboradores do setor de assistência técnica.')

# 👍
st.markdown('AVALIAR CONTEUDO')
avaliar= st.feedback('thumbs')
if avaliar == True:
    st.balloons()

st.sidebar.metric(label="ATENDIMENTOS", value=42, delta= '3.8%', delta_color= 'normal')
st.sidebar.divider()
st.sidebar.metric(label="REVISOES PREÇO FIXO", value=21, delta= '2.5%', delta_color= 'normal')
st.sidebar.divider()
st.sidebar.metric(label="SERVIÇOS FORA DE GARANTIA", value=18, delta= '3.8%', delta_color= 'normal')
st.sidebar.divider()
st.sidebar.metric(label="OUTROS", value=3, delta= '-1.3%', delta_color= 'normal')
st.sidebar.divider()
