import streamlit as st
import random
from iqoptionapi.stable_api import IQ_Option
from datetime import date
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.trend import SMAIndicator
from ta.trend import EMAIndicator
import time
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
from collections import Counter

st.set_page_config(page_title="AlphaSum Algorithm", page_icon=":moneybag:",layout="wide")
today_str = date.today().strftime("%Y-%m-%d")
start_date = date.today() - timedelta(days = 3)
end_date = date.today() + timedelta(days = 5)  
hide_st_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
   

st.title("🏦 IQ Option Login")
#Iq=IQ_Option("mashkim854@gmail.com","Mk@34676966@")
left_column,right_column = st.columns(2)
with left_column:
    email1 = st.text_input("Email Address")
with right_column:
    pword1 = st.text_input("Enter a password", type="password")
    # Check if the username and password are valid
left_column,right_column,c2,c3 = st.columns(4)
with left_column:
    account = st.radio("Choose Account Type",('Practice', 'Real'))
    if account == 'Real':
        st.success('This Account Option is available for a limited time only. Terms and Conditions Apply')
    else:    
        st.success("This Account Option is available.")
with right_column:
    goaloptions=["EURUSD","EURJPY","EURGBP","AUDUSD","AUDJPY","AUDCAD","GBPJPY","GBPUSD","USDJPY"]
    goal=st.selectbox("Choose Currency Pair", options=goaloptions)
with c2:
    initialmoney=st.number_input("Start trading at amount of ", min_value=1, max_value=10, step=1, value=1, disabled=False, label_visibility="visible")
    if initialmoney>5:
        st.warning('Warning: When trading amount is too high, risk of loss is also high', icon="⚠️")
with c3:
    timeframe=st.number_input("Candlestick Expiration timeframe in minutes", min_value=1, max_value=10, step=1, value=1, disabled=False, label_visibility="visible")
if st.button('Start Trading Robot'):
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
        placeholder = st.empty()
        while True:
            with placeholder.container():
                end_from_time=time.time()
                a=((int(timeframe))*15)
                data=Iq.get_candles("EURUSD", a, 100, end_from_time)
                df=pd.DataFrame(data)
                close100=(df.iloc[99][5])
                left_column,right_column= st.columns(2)
                with left_column:
                    indicator_bb = BollingerBands(close=df["close"], window=20, window_dev=2)
                    df['bb_bbm'] = indicator_bb.bollinger_mavg()
                    df['bb_bbh'] = indicator_bb.bollinger_hband()
                    df['bb_bbl'] = indicator_bb.bollinger_lband()
                    bbm100=(df.iloc[99][9])
                    bbh100=(df.iloc[99][10])
                    bbl100=(df.iloc[99][11])
                    st.header("BOLINGER BANDS")
                    if close100<bbl100:
                        bb="buy"
                        st.write("Bolinger Band: Buy")
                    elif close100<bbm100:
                        bb="0"
                        st.write("Bolinger Band: Weak Buy")
                    elif close100>bbh100:
                        bb="sell"
                        st.write("Bolinger Band: Sell")
                    elif close100>bbm100:
                        bb="0"
                        st.write("Bolinger Band: Weak Sell")
                    else:
                        bb="0"
                        st.write("Bolinger Band: Error")
                with right_column:
                    indicator_rsi = RSIIndicator(close=df["close"], window=14)
                    df["RSI"]=indicator_rsi.rsi()
                    rsi100=(df.iloc[99][12])
                    st.header("RSI")
                    if rsi100>80:
                        rsi="Sell"
                        st.write("RSI : Strong Sell")
                    elif rsi100>70:
                        rsi="Sell"
                        st.write("RSI : Sell")
                    elif rsi100<20:
                        rsi="Buy"
                        st.write("RSI : Strong Buy")
                    elif rsi100<30:
                        rsi="Buy"
                        st.write("RSI : Buy")
                    else: 
                        rsi="0"                        
                        st.write("RSI : Condition not met")

                left_column,right_column= st.columns(2)
                with left_column:
                    indicator_macd = MACD(close=df["close"], window_slow=26, window_fast=12, window_sign=9)
                    df["MACD LINE"]=indicator_macd.macd()
                    df["MACD HISTOGRAM"]=indicator_macd.macd_diff()
                    df["MACD SIGNAL LINE"]=indicator_macd.macd_signal()
                    macdline100=(df.iloc[99][13])
                    machist100=(df.iloc[99][14])
                    macdsig100=(df.iloc[99][15])
                    macdline99=(df.iloc[98][13])
                    machist99=(df.iloc[98][14])
                    macdsig99=(df.iloc[98][15])
                    st.header("MACD")
                    if macdline99<macdsig99 and macdline100>macdsig100 and machist100<0:
                        macd="Buy"
                        st.write("MACD : Strong Buy")
                    elif macdline100>macdsig100 and machist100<0:
                        macd="Buy"
                        st.write("MACD : Buy")
                    elif macdline99>macdsig99 and macdline100<macdsig100 and machist100>0:
                        macd="Sell"
                        st.write("MACD : Strong Sell")
                    elif macdline100<macdsig100 and machist100>0:
                        macd="Sell"
                        st.write("MACD : Sell")
                    else:
                        macd="0"
                        st.write("MACD : Condition not met")
                with right_column:
                    indicator_SMA = SMAIndicator(close=df["close"], window=20)
                    df["SMA"]=indicator_SMA.sma_indicator()
                    indicator_EMA = EMAIndicator(close=df["close"], window=20)
                    df["EMA"]=indicator_EMA.ema_indicator()
                    sma100=(df.iloc[99][16])
                    ema100=(df.iloc[99][17])
                    sma90=(df.iloc[89][16])
                    ema90=(df.iloc[89][17])
                    st.header("MOVING AVERAGES")
                    if sma90>ema90 and sma100<ema100:
                        ma="Sell"
                        st.write("Moving Average : Strong Sell")
                    elif sma90<ema90 and sma100>ema100:
                        ma="Buy"
                        st.write("Moving Average : Strong Buy")
                    elif (abs(sma90-ema90))>(abs(sma100-ema100)):
                        ma="Sell"
                        st.write("Moving Average : Possible Sell")
                    elif (abs(sma90-ema90))<(abs(sma100-ema100)):
                        ma="Buy"
                        st.write("Moving Average : Possible Buy")
                    else:
                        ma="0"
                        st.write("Moving Average : Condition not met") 
                counter = Counter([ma, rsi, macd, bb])
                buy_count = counter["Buy"]
                sell_count = counter["Sell"]
                if buy_count >= 3:
                    decision = "Buy"
                if sell_count >= 3:
                    decision = "Sell"
                else:
                    decision = "0"
                st.write("Decision = ",decision)
                time.sleep(timeframe*3)
                if decision=="Sell":
                    check1,id1=Iq.buy(Money1,goal,"put",timeframe)
                    if check1:
                        check1_result="success"
                    else:
                        check1_result="failed"
                        time.sleep(2)
                        check1,id1=Iq.buy(Money1,goal,"put",timeframe)
                    status1,profpercent1=Iq.check_win_v4(id1)
                    if status1=="win":
                        Money1=initialmoney
                    else:
                        Money1=Money1*2.5
                elif decision=="Buy":
                    check1,id1=Iq.buy(Money1,goal,"call",timeframe)
                    if check1:
                        check1_result="success"
                    else:
                        check1_result="failed"
                        time.sleep(2)
                        check1,id1=Iq.buy(Money1,goal,"call",timeframe)
                    status1,profpercent1=Iq.check_win_v4(id1)
                    if status1=="win":
                        Money1=initialmoney
                    else:
                        Money1=Money1*2.5
                else:
                    st.write("No trade")
else:
    st.write('Push Button to start Robot')


