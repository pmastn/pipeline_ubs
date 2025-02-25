import streamlit as st
import pandas as pd
import plotly.express as px

# PEDRO MASTANDREA RA10389910

# Carregar o arquivo atualizado
df = pd.read_csv("ubs_atualizado.csv", sep=";")

# Contar a frequência de UBS por estado
df_freq = df['Nome_UF'].value_counts().reset_index()
df_freq.columns = ['Estado', 'Frequência']

# Criar o dashboard
st.title("Dashboard de Unidades Básicas de Saúde")

# Gráfico de barras
grafico = px.bar(df_freq, x='Estado', y='Frequência', 
                 title='Frequência de UBS', 
                 labels={'Estado': 'Estado', 'Frequência': 'Número de UBS'},
                 text_auto=True)

st.plotly_chart(grafico)

# Filtro para estados específicos
estados = st.multiselect("Selecione os estados", df['Nome_UF'].unique())

if estados:
    df_filtrado = df[df['Nome_UF'].isin(estados)]
    st.write("Estados selecionados:", estados)
    st.write("Número de UBS após filtro:", len(df_filtrado))
    st.write(df_filtrado)
else:
    df_filtrado = df 
     

# # EX 1 Mapa de dispersão

# Substituir vírgulas por pontos e converter para num
df['LATITUDE'] = df['LATITUDE'].str.replace(',', '.').astype(float)
df['LONGITUDE'] = df['LONGITUDE'].str.replace(',', '.').astype(float)


mapa = px.scatter_mapbox(df_filtrado, 
                         lat='LATITUDE',  
                         lon='LONGITUDE', 
                         hover_name='Nome_Município',  # Nome do município passando mouse
                         hover_data={'Nome_UF': True},
                         zoom=3,  # Zoom inicial
                         title='Mapa de dispersão das UBS')

mapa.update_layout(mapbox_style="open-street-map")  # tipo do mapa
mapa.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})  # margens para o mapa
st.plotly_chart(mapa)

# EX2 Gráfico de Pizza
grafico_pizza = px.pie(df_freq, values='Frequência', names='Estado', title='Percentual de frequência por estado')
st.plotly_chart(grafico_pizza)

# EX3 

# Contando numero de UBS por municipio
df_municipios = df['Nome_Município'].value_counts().reset_index()
df_municipios.columns = ['Município', 'Numero de Ubs']

# Filtrando com controle deslizante
valor_atual_filtro = st.slider('Filtrar Municípios pelo mínimo de UBS', min_value=1, max_value=df_municipios['Numero de Ubs'].max(), value=1)
df_filtradoMin = df_municipios[df_municipios['Numero de Ubs'] >= valor_atual_filtro]

# Criar histograma
histograma = px.histogram(df_filtradoMin, x='Numero de Ubs',
                          title=f'Distribuição de Municípios por Número de UBS (Mínimo de {valor_atual_filtro} UBS)',
                          labels={'Numero de Ubs': 'Número de UBS', 'count': 'Número de Municípios'},
                          nbins=25)
st.plotly_chart(histograma)