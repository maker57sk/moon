
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


    col1, col2, col3, col4 = st.beta_columns(4)


    with col1:

        # Embed a youtube video
        st_player("https://youtu.be/CmSKVW1v0xM")
    
    with col2:

        # Embed a music from SoundCloud 
        st_player("https://soundcloud.com/imaginedragons/demons")

    with col4:

        # Embed a youtube video
        st_player("https://www.youtube.com/watch?v=1uXIeLmdM_M&list=PLbky1Uo8tP8DVkZicszACTrYKmhZG_4Av&index=6")

        
    with col3:

         # Embed a youtube video
        st_player("https://www.youtube.com/watch?v=U8EtBFiJ0JE&list=PLbky1Uo8tP8DVkZicszACTrYKmhZG_4Av&index=2")


