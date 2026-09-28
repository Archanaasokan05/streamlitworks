import streamlit as st

st.title("BMI Value")

w=st.number_input("Enter weight(kg):")
h=st.number_input("Enter  height(cm):")
btn=st.button("Calculate")

# bmi = weight / ((height / 100) ** 2)
if btn:
    bmi=w/((h/100)**2)
    st.write("BMI=",bmi)
    if bmi<18.5:
        st.info("Under Weight")
    elif 18.5<=bmi<25:
        st.success("Normal")
    elif 25<=bmi<30:
        st.warning("Over Weight")
    elif bmi>30:
        st.error("Obesity")