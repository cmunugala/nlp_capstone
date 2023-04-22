
import streamlit as st

st.title('Rule Based Model')
st.write("""
A simple rules based model based on word counts can still yield powerful results. After pre-processing and extracting the words that occur around the word “laceration” in each report. We find which words occur disproportionately in one class over the other. Words that occur more in discharge reports where a procedure note is needed are deemed as contributing towards a positive classification, while words that occur more in reports where a procedure not is not needed contribute to a negative classification.
For predictions, we simply tabulate the score of the words from a prediction example and decide on the threshold of words to include.
""")
