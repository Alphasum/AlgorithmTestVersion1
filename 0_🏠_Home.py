import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import os

st.set_page_config(page_title="AlphaSum Algorithm", page_icon=":house_with_garden:",layout="wide")
image = Image.open(f'{os.getcwd()}/pages/logo2.jpeg')
st.sidebar.image(image, width=200,use_column_width= 500)
title0,title1,title2 = st.columns([1,3, 1])
with title1:
    image = Image.open(f'{os.getcwd()}/pages/logo.jpeg')
    st.image(image, width=400,use_column_width= 1000)
with title2:
        url2 = requests.get("https://assets3.lottiefiles.com/packages/lf20_96bovdur.json") #working
        if url2.status_code == 200:
            url_json = url2.json()
            st_lottie(url_json,speed=2,loop=True,quality="low",height=200,width=200)
        else:
            print("Error in the URL")
            
    
hide_st_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("About The Software ")
st. markdown(
    """Welcome to AlphaSum Algorithm - the ultimate trading robot software that has been designed to revolutionize the binary options market. Our sophisticated software has been developed to provide a consistent return on investment, so you can sit back and watch your profits grow.

Our expert team of traders has spent countless hours perfecting AlphaSum Algorithm's trading strategy, ensuring that it can handle even the most volatile market conditions. With its lightning-fast speed and precision, this robot will trade on your behalf with ruthless efficiency, maximizing your profits and minimizing your risks.

Whether you're a seasoned trader or a complete beginner, AlphaSum Algorithm is the perfect tool for you. Our intuitive interface and user-friendly design make it easy to set up your trading parameters and let the robot do the rest. Say goodbye to complicated trading charts and analysis - AlphaSum Algorithm takes care of everything for you.

With a $1 per minute return on investment, the possibilities are endless. Join the thousands of satisfied traders who are already using AlphaSum Algorithm to achieve their financial goals. With our powerful software, you can take control of your financial future and start seeing results today.

Try AlphaSum Algorithm now and experience the benefits of this powerful trading robot for yourself. With our proven track record and commitment to excellence, you can trust us to help you achieve your financial goals.

    """, unsafe_allow_html=True
) 
st.markdown("---")

st.title("TERMS AND CONDITIONS")
st. markdown(
    """
    Welcome to AlphaSum Algorithm. By accessing or using our trading robot services, you agree to be bound by the following terms and conditions.

 **✔️ Trading Robot Services**

We offer trading robot services for securities on binary option markets, subject to availability and applicable regulations. By using our services, you acknowledge that trading in securities involves a high degree of risk and may not be suitable for all investors.

**✔️ Eligibility**

To use our services, you must be at least 18 years old and have the legal capacity to enter into binding contracts. You may not use our services if you are a resident of a restricted jurisdiction or prohibited from using our services by applicable law.

**✔️ Account Registration**

To use our services, you must register for an account and provide accurate and complete information. You are responsible for maintaining the confidentiality of your account information, including your password. You agree to notify us immediately of any unauthorized use of your account.

**✔️ Trading Rules**

You agree to comply with all applicable trading rules and regulations when using our services. You are solely responsible for all trading decisions and actions taken using your account. We are not responsible for any losses or damages resulting from your trading decisions or actions.

**✔️ Fees**

We charge fees for our services, including subscription fees and account maintenance fees. You agree to pay all fees associated with your use of our services. We may change our fees at any time by providing notice to you.

**✔️ Intellectual Property**

All content on our website and trading robot platform, including text, graphics, logos, and software, is the property of AlphaSum Algorithm or its licensors and is protected by copyright and other intellectual property laws. You may not copy, reproduce, distribute, or create derivative works from our content without our prior written consent.

**✔️ Limitation of Liability**

To the maximum extent permitted by law, AlphaSum Algorithm is not liable for any direct, indirect, incidental, special, or consequential damages arising out of or in connection with your use of our services, including any losses resulting from trading in securities.

**✔️ Indemnification**

You agree to indemnify and hold AlphaSum Algorithm, its directors, officers, employees, and agents harmless from any claims, damages, losses, or expenses arising out of or in connection with your use of our services or violation of these terms and conditions.

**✔️ Termination**

We may terminate or suspend your account and access to our services at any time, without notice or liability, for any reason. You may also terminate your account at any time by notifying us.

**✔️ Governing Law and Jurisdiction**

These terms and conditions are governed by and construed in accordance with the laws of the jurisdiction where AlphaSum Algorithm is located. Any dispute arising out of or in connection with these terms and conditions shall be resolved through arbitration in accordance with the rules of the governing arbitration body.

**✔️ Amendments**

We may update these terms and conditions from time to time by posting a new version on our website. Your continued use of our services after any such changes constitutes acceptance of the updated terms and conditions.

**✔️ Contact Us**

If you have any questions or concerns about these terms and conditions or the use of our services, please contact us.

    """, unsafe_allow_html=True
) 

st.title("Privacy Policy ")
st. markdown(
    """
At AlphaSum Algorithm, we value the privacy of our customers and are committed to protecting their personal information. This privacy policy outlines how we collect, use, and disclose personal information in connection with our trading services.

**⭕ Collection and Use of Personal Information**

We may collect personal information from our customers, such as their name, address, email address, phone number, and financial information, in order to provide trading services. We may also collect information about a customer's trading activity, including transaction history and account balance. We use this information to:

- Provide trading bot services and support
- Comply with legal and regulatory requirements
- Prevent fraudulent activity
- Improve our services

**⭕ Disclosure of Personal Information**

We may disclose personal information to third parties in order to provide trading services or comply with legal and regulatory requirements. This may include:
- Financial institutions, such as banks and payment processors, to process transactions
- Regulators, such as securities commissions, to comply with reporting and other requirements
- Service providers, such as IT support and marketing firms, to assist with business operations
We will only disclose personal information to third parties who have agreed to maintain the confidentiality and security of the information.

**⭕ Security of Personal Information**

We take reasonable measures to protect personal information from loss, theft, and unauthorized access, disclosure, or modification. This includes physical, electronic, and procedural safeguards. However, no method of transmission over the internet or electronic storage is 100% secure, and we cannot guarantee the absolute security of personal information.

**⭕ Retention of Personal Information**

We retain personal information only for as long as necessary to fulfill the purposes for which it was collected or as required by law. When personal information is no longer needed, we will securely destroy or anonymize it.

**⭕ Access to and Correction of Personal Information**

Customers have the right to access and correct their personal information in our possession. To request access to or correction of personal information, please contact us using the contact information provided below.

**⭕ Changes to Privacy Policy**

We may update this privacy policy from time to time by posting a new version on our website. Customers should review the policy periodically for changes.

**⭕ Contact Us**

If you have any questions or concerns about our privacy policy or the collection, use, or disclosure of personal information, please contact us at [insert contact information].



**⭕ Risk Statement**

Please note that trading in securities involves a high degree of risk, and may not be suitable for all investors. The value of investments can go up or down, and past performance is not necessarily indicative of future results. Before investing in any securities, customers should carefully consider their investment objectives, risk tolerance, and financial situation. Customers should also read and understand all information about the security, including the risks involved, before making any investment decisions. AlphaSum Algorithm does not provide investment advice and makes no guarantees about the performance of any security. Customers should seek advice from a qualified financial advisor before making any investment decisions.


    """, unsafe_allow_html=True
) 
