import streamlit as st

st.title("Division")

num1=st.number_input("Enter number1:",min_value=0)
print(num1)
num2=st.number_input("Enter number2:",min_value=0)
print(num2)
btn=st.button("Div")
if btn:
    result=num1/num2
    # print(result)
    st.write("Division is ",result)
