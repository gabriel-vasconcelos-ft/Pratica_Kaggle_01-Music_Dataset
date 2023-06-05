import numpy as np
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
plt.title('Gráfico de Contagem da Popularidade')
plt.xticks(rotation=30)
st.pyplot(fig)
