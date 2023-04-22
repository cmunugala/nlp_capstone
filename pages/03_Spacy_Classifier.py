
import streamlit as st

st.title('Rule Based Model')
st.write("""
The spaCy and Classy-Classifier packages allow us to easily create a pipeline for text classification. This case we feed the full sentences and the class that it belongs to for each training example in dictionary format and simply choose which model to apply. We tried both en_core_web_lg and sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (transformer based model).

Predictions are in the form of probabilities that a text example belongs to one class of the other. We tune the model by choosing the threshold on which to accept an example as positive or negative class.
  
https://spacy.io/universe/project/classyclassification

""")
