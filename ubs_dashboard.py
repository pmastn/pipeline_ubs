import plotly
import plotly.exceptions
import plotly.express
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

# Mapa de dispersão

# EX2 Grafico de Pizza
grafico_pizza = plotly.express.pie(df_freq, values='Frequência', names='Estado', title='Percentual de frequência por estado')
st.plotly_chart(grafico_pizza)

# EX3 

# Contando numero de UBS por municipio
df_municipios = df['Nome_Município'].value_counts().reset_index()
df_municipios.columns = ['Município', 'Numero de Ubs']

# Filtrando com controle deslizante
valor_atual_filtro = st.slider('Filtrar Municipios pelo minimo de UBS',min_value=1, max_value=df.municipios['Numero de Ubs'].max(),value=1)
df_filtradoMin = df_municipios[df_municipios['Numero de Ubs'] >= valor_atual_filtro]


# Criar histograma
histograma = plotly.express.histogram(df_filtradoMin, x='Numero de Ubs',
                                      title='Distribuição de Municípios por Numero de UBS',
                                      labels={'Numero de UBS': 'Numero de UBS', 'count': 'Número de Municípios'},
                                      nbins=10)
st.plotly_chart(histograma)

# Filtro para estados específicos
estados = st.multiselect("Selecione os estados", df_freq['Estado'].unique())
if estados:
    df_filtrado = df[df['Nome_UF'].isin(estados)]
    st.write(df_filtrado)
