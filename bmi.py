import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Input: Weight in kilograms
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, format="%.2f")

# Input: Height in meters
height = st.number_input("Enter your height (in meters):", min_value=0.0, format="%.2f")

# Calculate BMI
if height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Determine BMI category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
else:
    st.info("Please enter a valid height.")