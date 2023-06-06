import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

base = pd.read_csv('songs.csv')

st.write(base)

fig, ax = plt.subplots(figsize=(7,5))
sns.histplot(base, x='Popularity', kde=True, color='b')
plt.xlabel('Popularidade')
plt.ylabel('Contagem')
plt.title('Histograma de Contagem da Popularidade')
st.pyplot(fig)


pop = base.head(12)['Name'].value_counts()
fig, ax = plt.subplots(figsize=(10,10))
sns.barplot(x=pop.index, y=pop.values)
plt.xlabel('Artista')
plt.ylabel('Contagem')
plt.title('Contagem de Artistas')
plt.xticks(rotation=60)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(5,5))
sns.barplot(data=base.head(15), x='Artist', y='Popularity')
plt.xticks(rotation=(90))
st.pyplot(fig)

