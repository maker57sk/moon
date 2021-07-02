# Import all modules
import references
from cheetsheets import pdcheet
import formscol
import projects
import ideas
import kitchenSink
import streamlit as st
from pyforest import *


# Title and headers
st.title('AIML UAE')
st.header('Artificial Intelligence & Machine Learning UAE')
st.sidebar.button('Home')


# Create a dictionary for sidebar page navigation with radio
PAGES = {
    "Projects": projects,
    "Ideas": ideas,
    "Kitchen Sink" : kitchenSink,
    "Forms" : formscol,
    "Cheetsheets": pdcheet,
    "References": references
}


# Navigation to work 
selection = st.sidebar.radio("Go To", list(PAGES.keys()) )
page = PAGES[selection]
page.app()
