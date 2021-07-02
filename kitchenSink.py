# Import modules
import streamlit as st


# Create App function 
def app():
    # Define header for the page
    st.header('Kitchen Sink')
                                                       
                          ##################################################################################         
                                                        # Forms in Columns
    st.subheader('Forms in columns')
    # Define grid coloumns
    col1, col2 = st.beta_columns(2)
              #----------------------------------------------------------------------------------------------------------#

    # First grid column
    with col1:
        with st.form('Form1'):
            st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
            st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
            submitted1 = st.form_submit_button('Submit 1')
              #----------------------------------------------------------------------------------------------------------#

    # Second grid column
    with col2:
        with st.form('Form2'):
            st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
            st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
            submitted2 = st.form_submit_button('Submit 2')
              #----------------------------------------------------------------------------------------------------------#


                          ##################################################################################         
                                                        # Columns in forms
    st.subheader('Columns in forms')
    # Create froms inside coulumn
    with st.form(key='columns_in_form'):
        cols = st.beta_columns(5)
        for i, col in enumerate(cols):
            col.selectbox(f'Make a Selection', ['click', 'or click'], key=i)
        submitted = st.form_submit_button('Submit')

                          ##################################################################################         
