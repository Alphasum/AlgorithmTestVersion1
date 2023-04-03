import streamlit as st
from pathlib import Path
from PIL import Image
import os.path
import os

current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()

SOCIAL_MEDIA = {
    "🐦 Twitter":"https://twitter.com/AlphaSumAlgori1",
    "📸 Instagram":"https://www.instagram.com/alphasumalgorithm/",
    "😀 Facebook":"https://facebook.com/Alphasum",
    
}

st.set_page_config(page_title=" AlphaSum Algorithm ", page_icon=":phone:",layout="wide")
st.title("📱 CONTACT US")
hide_st_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st. markdown ("""We understand that in today's fast-paced world, unexpected challenges can arise at any moment. That's why we want to remind you that we're here for you, no matter what.
Whether you have a question about our product or services, need assistance with subscription, or simply want to share your feedback with us, our team of dedicated professionals is always ready to help.

So, do not hesitate to contact us anytime, anywhere. We are available through multiple channels including email at alphasumalgorithm@yahoo.com, and social media. 
Our friendly and knowledgeable customer service representatives will listen to your concerns, provide solutions, and ensure that your experience with us is a positive one.

At AlphaSum Algorithm, we believe that our success is measured by the satisfaction of our clients. We are committed to providing exceptional service and support to every individual who chooses to work with us.
So, if you need anything at all, please do not hesitate to reach out via the links below. We look forward to hearing from you soon.""",unsafe_allow_html=True)

st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

image = Image.open(f'{os.getcwd()}/pages/logo2.jpeg')
st.sidebar.image(image, width=200,use_column_width= 500)
