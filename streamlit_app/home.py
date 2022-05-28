import pandas as pd
import streamlit as st

from config import datafields, home_image

#page functioning
def app():

    #heading and text information
    html1 = '''
    <style>
    #pred_image{
      
     }
    #heading{
      color: #E65142;
      text-align:top-left;
      font-size: 45px;
    }
    #sub_heading1{
    color: #E65142;
    text-align: right;
    font-size: 30px;
    }
    #sub_heading2{
    color: #E65142;
    text-align: left;
    font-size: 30px;
      }
    #usage_instruction{
    text-align: right;
    font-size : 15px;
    }
    #data_info{
    text-align : left;
    font-sixe : 15px;
    }
    /* Rounded border */
    hr.rounded {
        border-top: 6px solid #E65142;
        border-radius: 5px;
    }
    </style>
    <h1 id = "heading"> Rossmann Pharmaceuticals Sales Analysis </h1>
    <h3>Rossmann operates over 3,000 drug stores in 7 European countries.<br>
    </h3>
    '''
    st.markdown(html1, unsafe_allow_html=True)
    st.image(home_image, width=700, output_format="PNG")
    html2 = '''
    <hr class="rounded">
    <h3 id = "sub_heading1">The finance team is concerned with predicting their daily sales for up to six weeks in advance.</h3>
    '''
    st.markdown(html2, unsafe_allow_html=True)

    data=pd.read_csv('../data/eda/merged.csv')
    st.write(data.head(50))