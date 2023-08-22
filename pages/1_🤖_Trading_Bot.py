import streamlit as st
import pandas as pd
from ta.momentum import RSIIndicator
from iqoptionapi.stable_api import IQ_Option
import time 
import pandas as pd
import csv
from datetime import date
from datetime import datetime
import os

@st.cache_data
def rsioutcome():
    placeholder = st.empty()
    while True:
        with placeholder.container():
            end_from_time=time.time()
            Iq=IQ_Option(email1,pword1)
            Iq.connect() 
            data=Iq.get_candles("EURUSD", 15, 100, end_from_time)
            daf=pd.DataFrame(data)
            Iq.start_candles_stream("EURUSD", 15, 1)
            indicator_rsi = RSIIndicator(close=daf["close"], window=14)
            daf["RSI"]=indicator_rsi.rsi()
            #daf.to_csv("indicatordata.csv")
            rsi100=(daf.iloc[99][9])
            rsi99=(daf.iloc[98][9])
            st.write("rsi100 : ",rsi100)
            st.write("rsi99 : ",rsi99)
            if rsi100<70 and rsi99>70:
                outcome1="Sell"
                st.write("Sell success")
                return outcome1,rsi100,rsi99
                break
            elif rsi100>30 and rsi99<30:
                outcome1="Buy"
                st.write("Buy success")
                return outcome1,rsi100,rsi99
                break
            else:
                st.write("Running ...")
                time.sleep(15)
                k=False

st.set_page_config(page_title="AlphaSum Algorithm", page_icon=":moneybag:",layout="wide")
st.header("🏦 IQ Option RSI TEST")
goaloptions=["EURUSD","EURJPY","EURGBP","AUDUSD","AUDJPY","AUDCAD","GBPJPY","GBPUSD","USDJPY"]
goal=st.selectbox("Choose Currency Pair", options=goaloptions)
initialmoney=st.number_input("Start trading at amount of ", min_value=1, max_value=10, step=1, value=1, disabled=False, label_visibility="visible")
if initialmoney>5:
    st.warning('Warning: When trading amount is too high, risk of loss is also high', icon="⚠️")
Money1=initialmoney
left_column,right_column = st.columns(2)
with left_column:
    email1 = st.text_input("Email Address")
with right_column:
    pword1 = st.text_input("Enter a password", type="password")
    # Check if the username and password are valid
if email1=="" or pword1=="":
    st.error("Enter valid username and password")
else:
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
    now=datetime.now()
    end_time=now.replace(hour=23,minute=59,second=00)
    my_blc=Iq.get_balance()
    balaftstake=my_blc-Money1
    outcome="0"
    current_time=now.strftime("%H:%M:%S")
    today = date.today()
    df1 = pd.DataFrame({"date":[today],
                        "time":[current_time],
                        "Initial_balance":[my_blc],
                        "stake_1":[Money1],
                        "RSI position 1":[""],
                        "RSI position 2":[""],
                        "RSI outcome":[outcome],
                        "status_1":[""],
                        "balance_after_stake":[balaftstake],"Final_balance":[balaftstake]})
    file_exists = os.path.exists(f'Data_{email1}_{today}.csv')
    if file_exists==True:
        st.write("Backup file found and loaded")
    else:
        st.write("Creating new record file")
        df1.to_csv(f'Data_{email1}_{today}.csv',index=False)
        
        
    if iqch1==True:
        st.write(f"Log in successful")
        placeholder = st.empty()
        while True:
            with placeholder.container():
                end_from_time=time.time()
                expirations_mode=5
                k=False
                outcome,rsimax,rsimin=rsioutcome()
                if outcome=="Sell":
                    check1,id1=Iq.buy(Money1,goal,"put",expirations_mode)
                    if check1:
                        check1_result="success"
                    else:
                        check1_result="failed"
                        time.sleep(2)
                        check1,id1=Iq.buy(Money1,goal,"put",expirations_mode)
                    status1,profpercent1=Iq.check_win_v4(id1)
                    st.subheader(" 1st Trade Previous Result ")
                    st.subheader(f"{status1}")
                    st.markdown("---")
                    my_blcafter=Iq.get_balance()
                    if status1=="win":
                        Money1=initialmoney
                    else:
                        Money1=Money1*2.5
                elif outcome=="Buy":
                    check1,id1=Iq.buy(Money1,goal,"call",expirations_mode)
                    if check1:
                        check1_result="success"
                    else:
                        check1_result="failed"
                        time.sleep(2)
                        check1,id1=Iq.buy(Money1,goal,"call",expirations_mode)
                    status1,profpercent1=Iq.check_win_v4(id1)
                    st.subheader(" 1st Trade Previous Result ")
                    st.subheader(f"{status1}")
                    st.markdown("---")
                    my_blcafter=Iq.get_balance()
                    if status1=="win":
                        Money1=initialmoney
                    else:
                        Money1=Money1*2.5
                else:
                    st.write('condition not met')
                my_blc2=Iq.get_balance()
                df2 = pd.DataFrame({"date":[today],
                        "time":[current_time],
                        "Initial_balance":[my_blc2],
                        "stake_1":[Money1],
                        "RSI position 1":[rsimin],
                        "RSI position 2":[rsimax],
                        "RSI outcome":[outcome],
                        "status_1":[status1],
                        "balance_after_stake":[my_blcafter],"Final_balance":[my_blc2]})
                df = pd.read_csv(f'Data_{email1}_{today}.csv')
                df3 = pd.concat([df,df2], ignore_index = True)
                df3.to_csv(f'Data_{email1}_{today}.csv',index=False)

                        
