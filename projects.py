# Import modules
import streamlit as st


# Create App function
def app():

    # layout columns initialize
    projects, github = st.beta_columns(2)
    left, right = st.beta_columns(2)
    
    # First grid column
    with projects:
        st.header('Projects')
        # st.write('[projects](https://minicog.ai)')
        st.write('* A2T')
        st.write('* AIML UAE')
        st.write('* Ride Sharing')
        st.write('* Covid19')

    # Second grid column
    with github:    
        st.header('Libraries')
        st.write('* pyforest ')
        st.write('* yfinance')
        st.write('* numpy')

    # Third grid column
    with left:
        st.header('Ideas')
        st.subheader('Navigations')
        st.write('* Cheet sheets')
        st.write('* Videos')
        st.write('* papers')
    
    # Fouth grid column
    with right:
        st.header('AIML UAE')
        st.subheader('Vision')


