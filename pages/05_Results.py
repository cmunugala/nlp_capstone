import streamlit as st
import pandas as pd
import numpy as np

st.title('Results')
st.text(" ")
st.text(" ")
st.subheader('Here are the results from our different models:')
st.text(" ")
st.text(" ")

df = pd.DataFrame({'Rule-Based Model': [0.40,0.83],
                   'Spacy Model':[0.29,0.83],
                   'BERT':[0.53,0.83]}, index=['Precision','Recall'])

st.table(df)