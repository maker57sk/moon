
                                                    # APP Template
              #----------------------------------------------------------------------------------------------------------#

# Import modules
import streamlit as st
from streamlit_player import st_player


# Create App function 
def app():

    # App title
    st.title('Video')


              #----------------------------------------------------------------------------------------------------------#
    st.write('Welcome video')

    # Embed a youtube video
    st_player("https://youtu.be/CmSKVW1v0xM")

    # Embed a music from SoundCloud 
    st_player("https://soundcloud.com/imaginedragons/demons")


