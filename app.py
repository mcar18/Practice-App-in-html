import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

# Sidebar input
count = st.sidebar.slider("Select number of rows", 1, 100, 10)

# Generate sample data
df = pd.DataFrame({
    "x": range(count),
    "y": [i**2 for i in range(count)]
})

# Display table and chart
st.write("### Sample Data", df)
st.line_chart(df.set_index("x"))