import streamlit as st

st.logo('carmo.png')


def intro():
    st.title("Introdução")
    st.header('O Que é Análise de Dados?')
    st.markdown('''A análise de dados é um processo multifacetado que envolve a coleta, organização, interpretação e visualização de informações para identificar tendências, padrões e insights relevantes. Isso é essencial para tomar decisões embasadas em dados, otimizar processos e melhorar o desempenho em diversas áreas. A análise de dados não se limita apenas a dados numéricos, mas também lida com dados qualitativos, como texto e imagens, tornando-se uma ferramenta versátil para a extração de conhecimento a partir de uma variedade de fontes de informação. ''')

    st.header('Como a Análise de Dados Pode Melhorar a Tomada de Decisão?')
    st.markdown('''A tomada de decisões é o coração de qualquer organização. Uma decisão equivocada pode ter implicações significativas. É aí que a análise de dados entra em ação, permitindo:''')

    st.subheader('1. Reduzir a incerteza')
    st.markdown('''A análise de dados fornece informações precisas e confiáveis, eliminando a necessidade de tomar decisões com base em palpites. Exemplo Prático - Case Netflix: A Netflix usa análise de dados para recomendar filmes e séries com base no histórico de visualização dos usuários. Isso aumenta a retenção de clientes, pois os usuários encontram conteúdo relevante com mais facilidade.''')

    st.subheader('2. Identificar tendências e padrões')
    st.markdown('''A análise ajuda a identificar tendências emergentes e padrões ocultos nos dados. Exemplo Prático - Case Target: A varejista Target usou análise de dados para identificar mulheres grávidas com base em mudanças sutis de compra e enviou ofertas personalizadas. Isso demonstra como a análise pode identificar tendências de mercado antes mesmo de se tornarem óbvias.''')

    st.subheader('3. Avaliar o desempenho passado e presente')
    st.markdown('''A análise de dados permite avaliar o desempenho atual e passado da empresa. Exemplo Prático - Case Google: O Google usa análise de dados para monitorar o tráfego em seu mecanismo de busca, identificando picos e quedas que ajudam a ajustar seus algoritmos e fornecer melhores resultados aos usuários.''')
    st.divider()
    st.markdown('''Agora é a hora de agir. Comece avaliando como a análise de dados pode ser implementada em sua empresa. Explore as técnicas e ferramentas disponíveis e promova uma cultura de dados. Não deixe que a concorrência o supere – coloque a análise de dados no centro de sua estratégia de negócios e veja os benefícios se desdobrarem diante de seus olhos. A revolução dos dados já começou; junte-se a ela e garanta o futuro do seu negócio.''')


intro()

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
