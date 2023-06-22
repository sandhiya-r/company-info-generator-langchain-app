import streamlit as st
from ice_breaker import learn_about_company
from output_parsers import *

st.title('Company Info Finder')

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Enter the Company name')
  submitted = st.form_submit_button('Submit')

if __name__ == '__main__':
    print('Langchain starting!!')
    result = learn_about_company(submitted)
    parsed_result = parser.parse(result)
    print(parsed_result)
    st.info(parsed_result)