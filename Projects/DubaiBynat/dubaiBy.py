
                                                    # APP Template
              #----------------------------------------------------------------------------------------------------------#

# Import modules
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt



# Create App function 
def app():

    # App title
    st.title('Dubai Bynat')
    st.write('Welcome')

    fileUploading()

              #----------------------------------------------------------------------------------------------------------#

def fileUploading():
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
  
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)


        c1, c2 = st.beta_columns(2)

        with c1:
            # Select columns to plot using dropdown multiselect
            selected_columns = st.multiselect('Select columns to Plot', dataframe.columns)
            

            for col in selected_columns:
                new_df = dataframe[col]

                # st.write(new_df)

            # new_df = df[ (df['Club'].isin(clubs)) & (df['Nationality'].isin(national))]

            # Plot different graphs with checkbox
            if st.checkbox('Line'):
                with c2:
                    st.line_chart(new_df)
            if st.checkbox('Area'):
                with c2:
                    st.area_chart(new_df)
            if st.checkbox('Bar'):
                with c2:
                    st.bar_chart(new_df)

            new_plots(dataframe, col)


def new_plots(df, col):
    # Add some matplotlib code !
    fig, ax = plt.subplots()
    df.hist(
        bins=8,
        column=col,
        grid=False,
        figsize=(8, 8),
        color="#86bf91",
        zorder=2,
        rwidth=0.9,
        ax=ax,
        )
    st.write(fig)    



        
