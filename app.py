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

