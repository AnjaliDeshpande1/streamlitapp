import streamlit as st

st.title("Interactive Widgets Demo")

# Slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You selected: {age} years old")

# Button
if st.button("Click me!"):
    st.write("Button clicked!")

# Checkbox
if st.checkbox("Show details"):
    st.write("Details are now visible.")

# Selectbox (Dropdown)
options = ["Option A", "Option B", "Option C"]
selected_option = st.selectbox("Choose an option", options)
st.write(f"You chose: {selected_option}")

import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Visualization Example")

# Create a sample DataFrame
data = pd.DataFrame({
    'col1': np.random.rand(10),
    'col2': np.random.randint(1, 100, 10)
})

st.write("Here's a sample DataFrame:")
st.dataframe(data)

# Line Chart
st.write("Here's a line chart:")
st.line_chart(data['col1'])

# Bar Chart
st.write("Here's a bar chart:")
st.bar_chart(data['col2'])