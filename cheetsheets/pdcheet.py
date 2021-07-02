# Import modules
import pandas as pd
import streamlit as st



# Create app function

def app():


    # Define grid columns
    col1, col2, col3 = st.beta_columns(3)

    # 1st grid column
    with col1:
        st.header('Streamlit')
        # st.write('[streamCheet](https://streamlit-cheat-sheet.herokuapp.com)')

    # 2nd grid column
    with col2:
        st.header('Pandas')

    # 3rd grid column
    with col3:
        st.header('Pandas')