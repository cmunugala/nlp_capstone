import streamlit as st
import pandas as pd
import numpy as np

st.title('Results')
st.text(" ")
st.text(" ")
st.subheader('Here are the results from our different models:')
st.text(" ")
st.text(" ")

df = pd.DataFrame({'Rule-Based Model': [0,0,0],
                   'Spacy Model':[0,0,0],
                   'BERT':[0,0,0]}, index=['Precision','Recall','F1-Score'])

st.table(df)

st.text(" ")
st.text(" ")
st.subheader('Estimation of Money Lost from Procedures Not Billed:')
st.text(" ")
st.text(" ")