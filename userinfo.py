import streamlit as st

st.title("ENTER DETAILS")
name=st.text_input("Enter Name:")
age=st.number_input("Enter age:")
place=st.text_input("Enter place:")
gender=st.radio("Select Gender",['Male','Female'])
qualification=st.selectbox("Select Qualification",['BBA','BCA','BTECH'])
btn=st.button("Submit")
if btn:
    st.success("USER INFO")
    # st.subheader(f"Name is {name}\n Age={age}")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("Place:",place)
    st.write("Gender:",gender)
    st.write("Qualification:",qualification)
