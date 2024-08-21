import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title='My Streamlit Web App', page_icon="streamlit",layout="wide")

def loader_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css('style/style.css')
lottie_coding = loader_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
image_1 = Image.open('images/img1.jpeg')

# ------ Header Section ------
with st.container():
    st.subheader('Hi, I am the Matin')
    st.subheader('Django Backend Developer from Azerbaijan :wave:')
    st.write('I use Python, Django, Flask, PostgreSQL, OracleSQL')
    st.write('[Learn More >](https://github.com/MetinQardasov11)')


# ------ Projects Section ------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write('')
        st.write(
            """
            My Github Projects:
            - Tevhid Makale
            - Django Ecommerce
            - Django Product App
            """
        )
        st.write('[Linkedin >](https://www.linkedin.com/in/matin-gardashov-1130bb225/)')
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
        
with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_1)
    
    with text_column:
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            """
        )
        st.markdown("[GitHub Link >](https://github.com/MetinQardasov11)")
        
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_1)
    
    with text_column:
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            """
        )
        st.markdown("[GitHub Link >](https://github.com/MetinQardasov11)")
        

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    
    contact_form = """
    <form action="https://formsubmit.co/metin.qardasov2003@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()