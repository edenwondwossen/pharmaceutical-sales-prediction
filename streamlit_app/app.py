import streamlit as st

import home
import data_visualization
import model
from config import nav_image

#Pages in the app
PAGES = {
    "Home": home,
    "Data Visualization": data_visualization,
    "Data Prediction": model
}

#background styling
page_bg = '''
<style>
body {
background-color : #f4f4f4;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

#navbaar styling
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#292929,#E65142;9);
    color: black;
    align-text: center;
}
hr.rounded {
        border-top: 6px solid #E65142;
        border-radius: 5px;
    }
.img{
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
}
</style>
""", unsafe_allow_html=True,
)

#inseting image in the sidebar
st.sidebar.image(nav_image, width =150)

#navbar content-1
html3 = '''
<h2 style="text-align: center;"> Exploare anything and everything!</h2>
<hr class="rounded">
'''
st.sidebar.markdown(html3, unsafe_allow_html=True)

st.sidebar.title("Explore")

#radio selection for the pages
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

#navbar content-2
html4 = '''
<br>
<br>
<p><b>Data Visualization -</b> Analyze the sales data across various types of analysis methods for <i>Rossmann Stores</i> using 
multiple graphs</p>
<br>
<p><b>Data Prediction -</b> Predict the future sales set to different features or columns. Predictions can be made using default entries
or select one or multiple fields to be manually edited for predictions.</p>
'''  
st.sidebar.markdown(html4, unsafe_allow_html=True)