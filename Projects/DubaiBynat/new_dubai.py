
                                                    # APP Template
              #----------------------------------------------------------------------------------------------------------#

# Import modules
import streamlit as st
import pandas as pd 


# Create App function 
def app():

    # App title
    st.title('Dubai Bynat')

              #----------------------------------------------------------------------------------------------------------#
    st.write('Welcome')

    # Call the new functions here
    choosePlot()

def fileUploadFrom():
  
    uploaded_file = st.file_uploader("Upload Files", key = 'dataFileSal')
    if uploaded_file is not None:
        
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)

        dataframe = pd.read_csv(uploaded_file)

    return dataframe


# def dataRead():
    
#     df = fileUploadFrom()
#     # df = pd.read_csv(df_up)
    
    
#     # df = pd.read_csv('./data/GetDataSet.csv')
#     return df

def chooseCol():
    df = fileUploadFrom()
    st.write(df.columns)
    selectCol = st.multiselect('Choose columsn to plot', df.columns.unique())
    return selectCol

# function for choose the columns 
def chooseColumns():
    
    df = fileUploadFrom()
    st.write(df.columns)

    # df_plot1 = df.drop(['Category_EN', 'Category_AR'], axis=1)

    # st.line_chart(df_plot1)

    data = chooseCol()
    return data 



 # Function to choose and plot
def choosePlot():

    data = chooseColumns()

  # Checkbox for plotting different plots
    if st.checkbox('Line'):
        st.line_chart(data)
    if st.checkbox('Area'):
        st.area_chart(data)
    if st.checkbox('Bar'):
        st.bar_chart(data)




   
        