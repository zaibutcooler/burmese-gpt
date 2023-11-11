import streamlit as st

st.title("Burmese GPT")

user_input = st.text_area("Enter your text here:", "")

option = st.selectbox(
    'Select an option:',
    ('Option 1', 'Option 2', 'Option 3')
)

if st.button("Generate"):
    st.write("Generated text will appear here.")