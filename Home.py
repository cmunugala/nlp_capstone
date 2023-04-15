import streamlit as st
from PIL import Image



st.title("Identification of Procedure Note Requirements from Discharge Summaries")
st.subheader("Evan Chan, Khakali Olenja, Chetan Munugala")
st.text(" ")
st.text(" ")
st.write("""Welcome to the homepage for our UC Berkeley Capstone project. Here you will find background and details about how we used cutting 
         edge ideas in the field of Natural Language Processing to help diagnose a common issue in hospitals today!""")
    
im = Image.open("images/chetan.jpeg")
im = im.resize((500,500))
im2 = Image.open("images/chetan.jpeg")
im3 = Image.open("images/khakali.png")

#st.image([im,im2,im3], caption=['Chetan - UC Berkeley','hi','bye'],width=170)

col1, col2, col3 = st.columns(3)
with col1:
    st.image(im, caption = 'Chetan - UC Berkeley')
with col2:
    st.image(im2, caption = 'Evan - UC Berkeley')
with col3:
    st.image(im3, caption = 'Khakali - UC Berkeley')

st.text(" ")
st.text(" ")

st.subheader('Collaborators')
st.subheader('Aaron Kornblith, Karan Bains, Hope Shwartz, Newton Addo, Naina Sabbineni')
