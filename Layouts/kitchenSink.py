# Import modules
import streamlit as st
import streamlit.components.v1 as components


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
    
    
    st.write('[minicog.ai](https://minicog.ai)')


                          ##################################################################################         
                                                # Html embeded cards

# bootstrap 4 collapse example
    components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <div id="accordion">
        <div class="card">
            <div class="card-header" id="headingOne">
            <h5 class="mb-0">
                <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                Collapsible Group Item #1
                </button>
            </h5>
            </div>
            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
            <div class="card-body">
                Collapsible Group Item #1 content
            </div>
            </div>
        </div>
        <div class="card">
            <div class="card-header" id="headingTwo">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                Collapsible Group Item #2
                </button>
            </h5>
            </div>
            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
            <div class="card-body">
                Collapsible Group Item #2 content
            </div>
            </div>
        </div>
        </div>
        """,
        height=160,
    )

                          ##################################################################################         
    