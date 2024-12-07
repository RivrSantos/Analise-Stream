import streamlit as st
import pandas as pd
import pydeck as pdk

st.logo('carmo.png')


def maps():
    st.header('DISPERSAO DEMOGRAFICA', divider=True)
    st.markdown(''' Diante do atual cenário vale destacar a importância da dispersão geográfica para planejamento de campanhas de marketing e publicidade visando o fortalecendo da marca e a conquista de novos clientes''')
    st.divider()
    df = pd.DataFrame({
        'lat': [-16.69641120149624, -17.11615327640339, -16.718440856769977, -16.734519609574676, -16.7294971631257, -16.778051967668613, -16.723197848502167, -16.73931569364286, -16.700298156935425, -16.722586082835015, -16.694218504794108, -16.71735867946006, -16.545894473564132, -16.69715316642467, -22.429669928304584, -20.53436182099107, -16.755251857277372, -16.75174078693976, -16.743163430259067, -16.696285930653286, -16.713269398830658],
        'lon': [-43.81215144729478, -43.80891260497165, -43.872693433820174, -43.844793491492, -43.83387737614739, -43.868105904982144, -43.86416680021725, -43.86184634731103, -43.85606172905718, -43.8146690184754, -43.836719862657134, -43.817800962656335, -42.51433211089733, -43.83779254360566, -46.58162941450265, -54.67167891834721, -43.86953887799996, -43.889099171376635, -43.87884296080237, -43.851728429057815, -43.85951240313087]
    })
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=-16.69641120149624,
            longitude=-43.81215144729478,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
        ],
    ))

    st.info('🌎 . Os dados são de fonte local, demonstrando a dispersão geográfica de clientes em Montes Claros e região')


maps()

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
