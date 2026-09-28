import streamlit as st
from datetime import date

st.title("Registration form")
name=st.text_input("Enter Name:")
age=st.number_input("Enter your Age:",min_value=0)
dob=st.date_input("Date of Birth:",min_value=date(1990,1,1),
                  max_value=date.today(),value=date(2000,1,1))
email=st.text_input("Email:")
gender=st.radio("Select gender:",["Male","Female"])
course=st.selectbox("Select Course:",['Python','Java','Data Science'])
btn=st.button("Register")
if btn:
    st.success("STUDENT DETAILS")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",dob)
    st.write("Gender:",gender)
    st.write("Email:",email)
    st.write("Course:",course)
