import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import streamlit.components.v1 as com


st.title('BERT')

st.text(" ")
st.text(" ")

st.write("""
BERT is a relatively recent technological innovation in the field of Natural Language Processing that was created by Google.
BERT stands for Bidirectional Encoder Representations from Transformers. They are a family of language models that have 
made many tasks in Natural Language Processing easier. If you are interested in learning about BERT, Google provides some
good documentation here: https://cloud.google.com/ai-platform/training/docs/algorithms/bert-start#:~:text=BERT%20is%20a%20method%20of,question%20answering%20and%20sentiment%20analysis.
""")

st.text(" ")
st.text(" ")

st.write("""In addition I have found this video, along with others from Jay Alammar useful in understanding these models:""")

st.text(" ")
st.text(" ")

st.video("https://www.youtube.com/watch?v=ioGry-89gqE")

st.text(" ")
st.text(" ")

st.write("""
HuggingFace, a hub of open source models, makes it easy for someone to use one of these BERT models and fine tune it on a 
classification task, such as classifying whether or not a procedure not should have been created based on a discharge summary. 
In our project, we leveraged a BERT model to do exactly that. 
""")
 