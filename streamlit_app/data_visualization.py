import streamlit as st
import pandas as pd
import seaborn as sns

from config import univariate_1, univariate_2, univariate_3, univariate_4, bivariate_1, bivariate_2,bivariate_3,bivariate_4,bivariate_5,bivariate_6,bivariate_7, corr

#page functioning
def app():
    html1 = '''
            <style>
            #heading{
              color: #E65142;
              text-align:top-left;
              font-size: 45px;
            }
            </style>
            <h1 id = "heading"> Sales Data Analyses</h1>
        '''
    st.markdown(html1, unsafe_allow_html=True)

    #button functionality for data points
    col1, col2 = st.columns(2)
    analysis_type = col1.selectbox("Select the Analysis type", ('Univariate', 'Bivariate', 'Correlation'))
    data1 = col2.selectbox("Select the data visualization insight", ('univariate_1', 'univariate_2', 'univariate_3', 'univariate_4', 'bivariate_1', 'bivariate_2','bivariate_3','bivariate_4','bivariate_5','bivariate_6','bivariate_7', 'correlation'))
    if (analysis_type == 'Univariate'):
        if (data1 == 'univariate_1'):
           st.image(univariate_1)
        elif (data1 == 'univariate_2'):
            st.image(univariate_2)
        elif (data1 == 'univariate_3'):
            st.image(univariate_3)
        else:
            st.image(univariate_4)
    elif (analysis_type  == 'Bivariate'):
        if (data1 == 'bivariate_1'):
            st.image(bivariate_1)
        elif (data1 == 'bivariate_2'):
            st.image(bivariate_2)
        elif (data1 == 'bivariate_3'):
            st.image(bivariate_3)
        elif (data1 == 'bivariate_4'):
            st.image(bivariate_4)
        elif (data1 == 'bivariate_5'):
            st.image(bivariate_5)
        elif (data1 == 'bivariate_6'):
            st.image(bivariate_6)
        else:
            st.image(bivariate_7)
    else:
        if (data1 == 'correlation'):
            st.image(corr)
            

