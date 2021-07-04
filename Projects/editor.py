

                                                    # APP Template
              #----------------------------------------------------------------------------------------------------------#

# Import modules
import streamlit as st
import pandas as pd

from streamlit_ace import st_ace


# Create App function 
def app():

    # App title
    st.title('Editor')
    st.write('Welcome')

    newfunc()
    # somecode()

      #----------------------------------------------------------------------------------------------------------#
def newfunc():
    # Spawn a new Ace editor
    content = st_ace()

    # Display editor's content as you type
    content


# def somecode():


#     df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
#     pr = df.profile_report()

#     st_profile_report(pr)
