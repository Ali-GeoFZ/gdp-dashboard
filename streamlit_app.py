import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

st.title('Hallloo')

st.write('**Data Science Course 2024**')

df = pd.read_csv('data/Bastar Craton.csv')

cat_names = df.columns.tolist()[27:]

col1, col2 = st.columns(2)

with col1:
    el1 = st.selectbox('select element', cat_names)
    el2 = st.selectbox('selext elememt', cat_names)

with col2:
    fig = plt.figure()
    plt.scatter(df[el1]/1000, df[el2]/1000)
    st.pyplot(fig)


st.dataframe(df)




tab1, tab2 = st.tabs(["📈 links", "🗃 rechts"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with informations")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)