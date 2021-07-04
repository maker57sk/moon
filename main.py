# Import all modules
import streamlit as st

from cheetsheets import pdcheet
from Layouts import formscol, projects, ideas, kitchenSink, references, video
from Projects import home, editor
from Projects.DubaiBynat import dubaiBy
from Projects.Awsome import one

# from pyforest import *

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
    "References": references,
    "Projects-Home":home,
    "Video": video,
    "Dubai": dubaiBy,
    "Editor": editor,
    "Awsome": one

}

# Navigation to work 
selection = st.sidebar.radio("Go To", list(PAGES.keys()) )
page = PAGES[selection]
page.app()

