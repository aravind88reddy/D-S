import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('heloo darla')
st.markdown('mark mama :sunglasses:')
st.header('header :couple:')
st.code('import panda')
code = '''import numpy
import pandas'''
st.code(code)
output = st.button('click')
if output == True:
    st.markdown('clicked')

check = st.checkbox('agree')
if check == True:
    st.markdown('agreed')

vege = st.radio('what is vankay',('brinjal','tamato ','cabbage'))
st.markdown(vege)

funn = st.button('click here')
if funn == True:
    with st.spinner('Wait for it...'):

         time.sleep(5)
         st.success('Done!')

    st.balloons()

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
