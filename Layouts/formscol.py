# Import modules
import streamlit as st 



# Create App function 
def app():

    # Create froms inside coulumn
    with st.form(key='columns_in_form'):
        cols = st.beta_columns(5)
        for i, col in enumerate(cols):
            col.selectbox(f'Make a Selection', ['click', 'or click'], key=i)
        submitted = st.form_submit_button('Submit')