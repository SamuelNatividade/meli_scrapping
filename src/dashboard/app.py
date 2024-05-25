import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('/Users/samuelnatividade/Desktop/Projetos/meli_scrapping/src/data/quotes.db')

df = pd.read_sql_query('SELECT * FROM mercadolivre_items mi', conn)

## fechar conexao 
conn.close()


## titulo da aplicacao
st.title('KPIs principais do sistema')

col1, col2, col3 = st.columns(3)




## KPI1 Numero total de itens
total_itens = df.shape[0]
col1.metric(label = 'Numero total de itens', value = total_itens)

## KPI2  numero de marcas unicas
unique_brands = df['brand'].nunique()
col2.metric(label = 'Numero de marcas unicas', value = unique_brands)

## KPI3 preco medio em reais
average_new_price = df['new_price'].mean()
col3.metric(label = 'Preco medio R$', value = f'{average_new_price:.2f}')


## Mais marcas encontradas ate a pagina 10
st.subheader('Marcas mais encontradas ate a pagina 10')
col1, col2 = st.columns([4,2])

to_10_pages_brands = df['brand'].value_counts().sort_values(ascending = False)
col1.bar_chart(to_10_pages_brands)
col2.write(to_10_pages_brands)


## Preco medio por marca
st.subheader('Preco marca por marca')
col1, col2 = st.columns([4,2])
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending = False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)


## satisfacao por marca
st.subheader('Satisfacao por marca')
col1, col2 = st.columns([4,2])
df_non_zero = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending = False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)









