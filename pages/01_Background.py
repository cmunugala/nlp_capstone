import streamlit as st
from PIL import Image


im = Image.open("images/doctors.jpg")
im = im.resize((500, 500))
col1, col2 = st.columns(2)
with col1:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.title('Background')
with col2:
    st.image(im)



st.subheader('Problem:')
st.write("""Every day hospital, countless procedures are performed in the emergency room. Normally, every time a procedure occurs
in the emergency room, a procedure note is created that documents the procedure. This procedure note is later referenced and
can be used as verification that a procedure occured before charging a patient for that procedure. 

However, due to the frantic enviornment and lack of staff in the emergency room, doctors sometime forget to create the procedure
notes, which is not only a bad documentation practice, but can also cost the hospital money because they are unable to bill patients
for work done. 
""")
         


         
st.text(" ")
st.text(" ")

st.subheader("Solution")
st.write("""Ultimately, to solve this problem, a technological solution will likely need to be created that either reminds
         the doctor to write a procedure note, or is able to write the procedure note for the doctor. However, before
         a hospital or outside company invests resources into building a solution, it is important that they understand
         how big this problem is and how much money they could be saving.
         
         
The model we created will allow hospitals to determine how many procedure notes should have been created and compare that number
to how many were actually created. This will allow hospitals to assess whether or not this problem is worth solving. """)
