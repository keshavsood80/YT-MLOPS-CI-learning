import streamlit as st

# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square,cube and fifth power.")

# Get user input
n = st.number_input("Enter an integer", value=1, step=1)

# Calculate powers
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display results
st.write(f"Square of {n} is: {square}")
st.write(f"Cube of {n} is: {cube}")
st.write(f"Fifth power of {n} is: {fifth_power}")