import streamlit as st

# Title
st.title("➕ Add Two Numbers")

# Input fields
num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

# Button to trigger addition
if st.button("Calculate Sum"):
    result = num1 + num2
    st.success(f"The sum of {num1} and {num2} is {result}")
