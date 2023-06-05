import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

base = pd.read_csv('songs.csv')

grf_popularity = base['Popularity'].value_counts()
fig, ax = plt.subplots(figsize=(5,2))
sns.histplot(base, x='Popularity', kde=True, color='b')
#sns.barplot(x=grf_popularity.index, y=grf_popularity.values)
plt.xlabel('')
plt.ylabel('')
plt.title('Popularidade')
plt.xticks(rotation=30)
st.pyplot(fig)
