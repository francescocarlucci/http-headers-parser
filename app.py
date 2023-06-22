import re
import requests
import streamlit as st

st.set_page_config(
    page_title="HTTP Header Parser",
    page_icon="🚀"
)

def validate_url(url):
    
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if re.match(url_pattern, url):
        return True
    else:
        return False

st.header('HTTP Header Parser')

st.write('''
A super-minimal demo app to test Streamlit, a pure-python web development framework.

Insert a url down below, click the button and get the HTTP response headers of any site!
''')

with st.form("get_headers"):
   
   url = st.text_input('Insert any URL:', placeholder='https://www.python.org')

   submit = st.form_submit_button("Get Headers")
   
   if submit:

        if validate_url(url):

            response = requests.get(url)

            headers = response.headers

            for header, value in headers.items():
                
                st.code(header + ': ' + value)

        else:

            st.error("Invalid URL!")

st.divider()

st.write('Built with ❤️ by [Francesco Carlucci](https://francescocarlucci.com/)')