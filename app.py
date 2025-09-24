import streamlit as st
from utils.temp_conversions import (
    celsius_to_fahrenheit, celsius_to_kelvin,
    fahrenheit_to_celsius, fahrenheit_to_kelvin,
    kelvin_to_celsius, kelvin_to_fahrenheit
)

# Set page config
st.set_page_config(
    page_title="Temperature Converter 🌡️",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Temperature Converter")

# Step 1: Select input unit
input_unit = st.selectbox("Select input unit for temperature", ["°C", "°F", "K"])

# Step 2: Enter temperature value
input_value = st.number_input(f"Enter temperature in {input_unit}", value=0.0, format="%.2f")

# Step 3: Select output unit (exclude input unit)
units = ["°C", "°F", "K"]
units.remove(input_unit)
output_unit = st.selectbox("Select output unit for tempetrature", units)

# Step 4: Convert button
if st.button("Convert"):
    result = None

    if input_unit == "°C":
        if output_unit == "°F":
            result = celsius_to_fahrenheit(input_value)
        elif output_unit == "K":
            result = celsius_to_kelvin(input_value)

    elif input_unit == "°F":
        if output_unit == "°C":
            result = fahrenheit_to_celsius(input_value)
        elif output_unit == "K":
            result = fahrenheit_to_kelvin(input_value)

    elif input_unit == "K":
        if output_unit == "°C":
            result = kelvin_to_celsius(input_value)
        elif output_unit == "°F":
            result = kelvin_to_fahrenheit(input_value)

    # Step 5: Show result
    if result is not None:
        st.markdown(f"### Temperature of {input_value:.2f} {input_unit}  =  Temperature of {result:.2f} {output_unit}")