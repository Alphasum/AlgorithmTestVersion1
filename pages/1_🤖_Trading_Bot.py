import streamlit as st
import random
from iqoptionapi.stable_api import IQ_Option
from datetime import date
import time as t
from datetime import datetime
import pandas as pd
import plotly_express as px
import os.path
import requests
from streamlit_lottie import st_lottie
from datetime import date, timedelta
import pandas_market_calendars as mcal
from PIL import Image
import threading
import os
import uuid

# Define a dictionary to store session objects
sessions = {}

# Define a function to create a new session object for a user
def create_session(email1):
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"username": email1}
    return session_id

# Define a function to get the session object for a user
def get_session(session_id):
    if session_id in sessions:
        return sessions[session_id]
    else:
        return None
    
def main(session_id):
    session = get_session(session_id)

    if session is None:
        st.error("Invalid session ID")
    else:
        st.header("Welcome!")

# Define the logout function
def logout(session_id):
    if session_id in sessions:
        sessions.pop(session_id)
        st.success("Logged out successfully!")
    else:
        st.error("Invalid session ID")


class StoppableThread(threading.Thread):
    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

st.set_page_config(page_title="AlphaSum Algorithm", page_icon=":moneybag:",layout="wide")
image = Image.open(f'{os.getcwd()}/pages/logo2.jpeg')
st.sidebar.image(image, width=200,use_column_width= 500)
today_str = date.today().strftime("%Y-%m-%d")
start_date = date.today() - timedelta(days = 3)
end_date = date.today() + timedelta(days = 5)
nyse = mcal.get_calendar('NYSE')
nyse_schedule = nyse.schedule(start_date=start_date, end_date=end_date)
    
def countdown():
    now=datetime.now()
    current_time=int(now.strftime("%S"))
    for i in range((60-current_time),0,-1):
        print(f"{i}",end="\r",flush=True)
        t.sleep(1)
    t.sleep(20)

    
   
def cointoss():
    return random.choice(["Buy", "Sell"])

def timebot():
    if (n%2):
        decide="Buy"
    else:
        decide="Sell"
    return decide

def timebotdouble():
    if n==0 or n==1:
        decide="Buy"
    else:
        decide="Sell"
    return decide

def candlestrategy():
    cc=Iq.get_realtime_candles(goal,size)
    for k in list(cc.keys()):
        open=(cc[k]['open'])
        close=(cc[k]['close'])
        if close>open:
            decide="Sell"
        else:
            decide="Buy"
        return decide

def threewthreel():
    if n<3:
        decide="Buy"
    else:
        decide="Sell"
    return decide

def fourwfourl():
    if n<4:
        decide="Buy"
    else:
        decide="Sell"
    return decide
        

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


n=0
stopvar="GO"
# Get the session ID from the URL
session_id = st.experimental_get_query_params().get("session_id", [None])[0]
# If there is no session ID, show the login page
# Define the login page
if session_id is None:
    st.header("🏦 IQ Option Login 2.3")
    left_column,right_column = st.columns(2)
    with left_column:
        email1 = st.text_input("Email Address")
    with right_column:
        pword1 = st.text_input("Enter a password", type="password")
        # Check if the username and password are valid
    if email1=="" or pword1=="":
        st.error("Enter valid username and password")
    else:
        session_id = create_session(email1)
        Iq=IQ_Option(email1,pword1)
        iqch1,iqch2=Iq.connect() 
        if iqch2 == "2FA":
            st.write('##### 2FA enabled #####')
            st.write("An sms has been sent with a code to your number")
            code_sms = st.text_input("Enter the code received")
            iqchi, iqch2 = Iq.connect_2fa(code_sms)
            st.write('Verifying sms code')
        if iqch1==True:
            st.success("Logged in successfully!")
        else:
            st.error("Enter valid username and password")

# If there is a session ID, show the main page
if session_id is not None:
    main(session_id)

# Add a logout button
if session_id is not None:
    st.write("")
    if st.button("Logout"):
        logout(session_id)
        session_id = None
left_column,right_column,c1,c2,c3 = st.columns(5)
with left_column:
    genre = st.radio("Choose A Strategy",('Strategy One', 'Strategy Two','Strategy Three','Strategy Four','Strategy Five','Strategy Six'))

with right_column:
    genre2 = st.radio("Choose Account Type",('Practice', 'Real'))
    if genre2 == 'Real':
        st.success('This Account Option is available for a limited time only. Terms and Conditions Apply')
    else:    
        st.success("This Account Option is available.")
with c1:
    goaloptions=["EURUSD","EURJPY","EURGBP","AUDUSD","AUDJPY","AUDCAD","GBPJPY","GBPUSD","USDJPY"]
    goal=st.selectbox("Choose Currency Pair", options=goaloptions)
with c2:
    initialmoney=st.number_input("Start trading at amount of ", min_value=1, max_value=10, step=1, value=1, disabled=False, label_visibility="visible")
    if initialmoney>5:
        st.warning('Warning: When trading amount is too high, risk of loss is also high', icon="⚠️")
with c3:
    exp_profit=st.number_input("Expected daily profit amount ", min_value=100, max_value=10000, step=100, value=100, disabled=False, label_visibility="visible")

expander = st.expander("TERMS AND CONDITIONS")
expander. markdown(
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
terms = st.radio("I have read and agree with the terms and conditions below",('Disagree', 'Agree'))
if terms =='Agree':
    if st.button('Start Trading Robot'):
        url4 = requests.get("https://assets7.lottiefiles.com/packages/lf20_DVSwGQ.json") #working
        if st.button("Stop"):
            stopvar="STOP"
        if url4.status_code == 200:
            url4_json = url4.json()
            st_lottie(url4_json,speed=1,loop=True,quality="low",height=150,width=150)
        else:
            st.write("Error in the URL")
        st.markdown("---")
        if genre2=='Real':
            st.success("Real account activated")
            balance_type="REAL"
            Iq.change_balance(balance_type)
        else:
            st.success("Practice account activated")
            balance_type="PRACTICE"
            Iq.change_balance(balance_type)
        Money1=initialmoney #amount per option
        Money2=initialmoney
        size=60                     #60 second bars (Timeframe in seconds)
        maxdict=1                   #numbers of bars to get
        expirations_mode=1  
        now=datetime.now()
        end_time=now.replace(hour=23,minute=59,second=00)
        my_blc=Iq.get_balance()
        balaftstake=my_blc-(Money1+Money2)
        current_time=now.strftime("%H:%M:%S")
        today = date.today()
        df1 = pd.DataFrame({"date":[today],
                            "time":[current_time],
                            "Initial_balance":[my_blc],
                            "Strategy":[genre],
                            "stake_1":[Money1],
                            "Option_1":[""],
                            "status_1":[""],
                            "stake_2":[Money2],
                            "Option_2":[""],
                            "status_2":[""],
                            "balance_after_stake":[balaftstake],"Final_balance":[balaftstake]})
        file_exists = os.path.exists(f'Data_{email1}_{today}.csv')
        if file_exists==True:
            st.write("Backup file found and loaded")
        else:
            st.write("Creating new record file")
            df1.to_csv(f'Data_{email1}_{today}.csv',index=False)
        placeholder = st.empty()
        while now < end_time:
            with placeholder.container():
                my_blc2=Iq.get_balance()
                today = date.today()
                my_blc=Iq.get_balance()
                left_column,right_column,col_3 = st.columns(3)
                with left_column:
                    st.subheader(" Todays Date")
                    st.subheader(f"{today}")
                with right_column:
                    st.subheader(":money_with_wings: Account Balance ")
                    st.subheader(f"US ${my_blc:,}")
                with col_3:
                    df_perc = pd.read_csv(f'Data_{email1}_{today}.csv')
                    netprofit=my_blc-int(df_perc['Initial_balance'].values[:1])
                    profit_perc=(my_blc-(int(df_perc['Initial_balance'].values[:1])))/exp_profit*100
                    st.metric(label="Net Profit for today", value=f"${round(netprofit)}", delta=f"{round(profit_perc)}%")
                    st.write(f"Expected profit for today is ${exp_profit:,}")
                    if netprofit>exp_profit:
                        stopvar="STOP"
                        st.balloons()
                        st.success(f"Yay! 🎉🎈🎊  Your net profit is ${round(netprofit)}")
                if stopvar=="STOP":
                    stop_thread = StoppableThread()
                    stop_thread.stop()
                    st.success("Bot stopped successfully")
                st.markdown("---")
                balaftstake=my_blc-(Money1+Money2)
                left_column,right_column = st.columns(2)
                with left_column:
                    st.subheader(":dollar: 1st Trade Amount ")
                    st.subheader(f"US ${Money1:,}")
                with right_column:
                    st.subheader(":dollar: 2nd Trade Amount ")
                    st.subheader(f"US ${Money2:,}")
                st.markdown("---")
                if genre == 'Strategy One':
                    strategy=cointoss()
                elif genre =='Strategy Two':
                    strategy=timebot()
                    if n==3:
                        n=0
                    else:
                        n=n+1
                elif genre =='Strategy Three':
                    strategy=timebotdouble()
                    if n==3:
                        n=0
                    else:
                        n=n+1
                elif genre =='Strategy Four':
                    strategy=candlestrategy()
                elif genre =='Strategy Five':
                    strategy=threewthreel()
                    if n==5:
                        n=0
                    else:
                        n=n+1
                elif genre =='Strategy Six':
                    strategy=fourwfourl()
                    if n==7:
                        n=0
                    else:
                        n=n+1
                else:
                    st.write('Error occurred: Invalid Strategy given')
                outcome=strategy
                                   
                if outcome=="Sell":
                    check1,id1=Iq.buy(Money1,goal,"put",expirations_mode)
                    check2,id2=Iq.buy(Money2,goal,"call",expirations_mode)
                    if not isinstance(id1, int):
                        st.write(f"Error value: {id1}")
                        break
                    if not isinstance(id2, int):
                        st.write(f"Error value: {id2}")
                        break
                    option1="Sell"
                    option2="Buy"
                    if check1:
                        check1_result="success"
                    else:
                        check1_result="failed"
                        t.sleep(2)
                        check1,id1=Iq.buy(Money1,goal,"put",expirations_mode)
                    if check2:
                        check2_result="success"
                    else:
                        check2_result="failed"
                        t.sleep(2)
                        check2,id2=Iq.buy(Money2,goal,"call",expirations_mode)
                    countdown()
                    status1,profpercent1=Iq.check_win_v4(id1)
                    status2,profpercent2=Iq.check_win_v4(id2)
                    left_column,right_column = st.columns(2)
                    with left_column:
                        st.subheader(" 1st Trade Previous Result ")
                        st.subheader(f"{status1}")
                    with right_column:
                        st.subheader(" 2nd Trade Previous Result ")
                        st.subheader(f"{status2}")
                    st.markdown("---")
                    my_blcafter=Iq.get_balance()
                    if status1=="win":
                        Money1=initialmoney
                    else:
                        Money1=Money1*2.3
                        
                    if status2=="win":
                        Money2=initialmoney
                    else:
                        Money2=Money2*2.3
                    outcome="Sell" 
                else: 
                    check1,id1=Iq.buy(Money1,goal,"call",expirations_mode)
                    check2,id2=Iq.buy(Money2,goal,"put",expirations_mode)
                    if not isinstance(id1, int):
                        st.write(f"Error value: {id1}")
                        break
                    if not isinstance(id2, int):
                        st.write(f"Error value: {id2}")
                        break
                    option1="Buy"
                    option2="Sell"
                    if check1:
                        check1_result="success"
                    else:
                        check1_result="failed"
                        t.sleep(2)
                        check1,id1=Iq.buy(Money1,goal,"call",expirations_mode)
                    if check2:
                        check2_result="success"
                    else:
                        check2_result="failed"
                        t.sleep(2)
                        check2,id2=Iq.buy(Money2,goal,"put",expirations_mode)
                    countdown()
                    status1,profpercent1=Iq.check_win_v4(id1)
                    status2,profpercent2=Iq.check_win_v4(id2)
                    left_column,right_column = st.columns(2)
                    with left_column:
                        st.subheader(" 1st Trade Previous Result ")
                        st.subheader(f"{status1}")
                    with right_column:
                        st.subheader(" 2nd Trade Previous Result ")
                        st.subheader(f"{status2}")
                    st.markdown("---")
                    my_blcafter=Iq.get_balance()
                    if status1=="win":
                        Money1=initialmoney
                    else:
                        Money1=Money1*2.3
                        
                    if status2=="win":
                        Money2=initialmoney
                    else:
                        Money2=Money2*2.3
                    outcome="Sell" 
                my_blc3=Iq.get_balance()
                now=datetime.now()
                current_time=now.strftime("%H:%M:%S")
                df2 = pd.DataFrame({"date":[today],
                                "time":[current_time],
                                "Initial_balance":[my_blc2],
                                "Strategy":[genre],
                                "stake_1":[Money1],
                                "Option_1":[option1],
                                "status_1":[status1],
                                "stake_2":[Money2],
                                "Option_2":[option2],
                                "status_2":[status2],
                                "balance_after_stake":[my_blcafter],"Final_balance":[my_blc3]})
                df = pd.read_csv(f'Data_{email1}_{today}.csv')
                df3 = pd.concat([df,df2], ignore_index = True)
                st.subheader(":bar_chart:  Accounts Graph ")
                fig_balance_change = px.line(df3, x='time', y='Final_balance', title=' Account Balance over time',template='plotly_dark')
                st.plotly_chart(fig_balance_change)
                st.markdown("---")
                st.dataframe(df3)
                csv = convert_df(df3)
                st.download_button(label="📥 Download data as CSV",data=csv,file_name=f'Data_{email1}_{today}.csv',mime='text/csv',key=f"csv{now}")
                df3.to_csv(f'Data_{email1}_{today}.csv',index=False)
                df_perc = pd.read_csv(f'Data_{email1}_{today}.csv')
                netprofit=my_blc-int(df_perc['Initial_balance'].values[:1])
                now=datetime.now()
    else:
        st.write('Push Button to start Robot')
else:
    st.write("Agree to Terms and conditions to use the trading robot") 
if today_str in nyse_schedule.index:
    url = requests.get("https://assets6.lottiefiles.com/packages/lf20_ml0yft0o.json") #sleeping error 404
    if url.status_code == 200:
        url_json = url.json()
        st_lottie(url_json,speed=2,loop=True,quality="low",height=150,width=150)

    else:
        st.write("Error in the URL")

else:
    st.warning(f"{today_str}:  Today the markets are NOT open. Enjoy the weekend!!", icon="😴")
    url3 = requests.get("https://assets7.lottiefiles.com/packages/lf20_txli4cbw.json") #running
    if url3.status_code == 200:
        url_json = url3.json()
        st_lottie(url_json,speed=1,loop=True,quality="low",height=150,width=150)
    else:
        st.write("Error in the URL")
