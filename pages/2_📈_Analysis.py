import streamlit as st
import pandas as pd
import plotly_express as px
import os.path
import random
from iqoptionapi.stable_api import IQ_Option
from PIL import Image
import os

@st.cache_data
def compliment():
    return random.choice(["One of the differences between some successful and unsuccessful people is that one group is full of doers, while the other is full of wishers.",
                        "You cannot plow a field by turning it over in your mind. To begin, begin.",
                        "Mondays are the start of the work week which offer new beginnings 52 times a year!",
                        "Success usually comes to those who are too busy looking for it.",
                        "Your Monday morning thoughts set the tone for your whole week. See yourself getting stronger, and living a fulfilling, happier & healthier life.",
                        "If you believe something needs to exist, if it's something you want to use yourself, don't let anyone ever stop you from doing it.",
                        "There are three ways to ultimate success: The first way is to be disciplined. The second way is to be courageous. The third way is to be persistent.",
                        "Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.",
                        "I never dreamed about success. I worked for it.",
                        "Take your victories, whatever they may be, cherish them, use them, but don’t settle for them.",
                        "He that can have patience can have what he will.",
                        "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
                        "Everything you've ever wanted is sitting on the other side of fear.",
                        "Ideation without execution is delusion.",
                        "Success is getting what you want, happiness is wanting what you get."])

st.set_page_config(page_title="AlphaSum Algorithm", page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Analysis Dashboard")
hide_st_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

image = Image.open(f'{os.getcwd()}/pages/logo2.jpeg')
st.sidebar.image(image, width=200,use_column_width= 500)

left_column,right_column = st.columns(2)
with left_column:
    email = st.text_input("Email Address")
with right_column:
    pword1 = st.text_input("Enter a password", type="password")
    
date=st.date_input("Select a Date")

if st.button("Get Data"):
    Iq2=IQ_Option(email,pword1)
    iqch1,iqch2=Iq2.connect() 
    if iqch1==True:
        file_exists = os.path.exists(f'Data_{email}_{date}.csv')
        if file_exists==True:
            st.write(f"Log in successful. Backup file found and loaded successfully")
            df = pd.read_csv(f'Data_{email}_{date}.csv')
            unique_counts = pd.DataFrame({'count1': df['stake_1'].value_counts().size, 'count2': df['stake_2'].value_counts().size},index=['unique_counts'])
            counts1 = df['status_1'].value_counts()[['win', 'loose']]
            counts2 = df['status_2'].value_counts()[['win', 'loose']]
            st.subheader(":bar_chart:  Accounts Graph ")
            fig_balance_change = px.line(df, x='time', y='balance_after_stake', title=' Account Balance over time',template='plotly_dark')
            st.plotly_chart(fig_balance_change)
            expander = st.expander("Description of Account Balance Graph")
            expander.write("""
                The chart above shows the change in account balance over time.
                It basically increases over time throughout the day.
                """)
                    
            st.markdown("---")
            st.subheader(":chart: Graphs")
            left_column,right_column = st.columns(2)
            with left_column:
                fig_counts1 = px.bar(counts1, x=counts1.index, y=counts1.values, title='Outcomes of Trade 1',template='plotly_dark')
                fig_counts1.update_layout(width=300, height=400)
                st.plotly_chart(fig_counts1)

            with right_column:
                fig_counts2 = px.bar(counts2, x=counts2.index, y=counts2.values, title='Outcomes of Trade 2',template='plotly_dark')
                fig_counts2.update_layout(width=300, height=400)
                st.plotly_chart(fig_counts2)
                
            expander = st.expander("Description of Outcome Graphs")
            expander.write("""
                The bar graphs show the cumulative number of wins and loses that occur in a trade line. 
                There are two trade lines resulting from the two trades that are made every minute.
                """)
                    
            st.markdown("---")    
                
            st.subheader(":white_circle: Pie Charts")   
            left_column,right_column = st.columns(2)
            with left_column:
                fig_status1 = px.pie(df, values='stake_1', names='status_1', title='Percentage Amounts for Trade 1')
                fig_status1.update_layout(width=500, height=400)
                st.plotly_chart(fig_status1)
            with right_column:
                fig_status1 = px.pie(df, values='stake_2', names='status_2', title='Percentage Amounts for Trade 2')
                fig_status1.update_layout(width=500, height=400)
                st.plotly_chart(fig_status1)
            expander = st.expander("Description of Pie Charts of Percentage Amounts")
            expander.write("""
                The pie charts show the percentage of the amounts used to cover wins, loses and equal.  
                The norm is that the loses section should be between 70% to 95%. 
                This means that the trading robot successfully traded within the parameters of risk management.
                """)
            fig = px.bar(unique_counts, title='Graph of Trade Counts')
            st.plotly_chart(fig)
            expander = st.expander("Description of Trade Counts Graph")
            expander.write("""
                This Graph shows the cumulative number of counts of buy and sell signals given by the trading robot  
                This should exist as a 50/50 count.
                This means that the trading robot successfully traded twice every minute.
                """)
            st.subheader(":ledger: Raw Data")
            st.dataframe(df)
                
            hide_st_style="""
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_st_style, unsafe_allow_html=True)
        else:
            st.warning('Invalid Date entred.', icon="⚠️")
    else:
        st.warning("Log in failed. Try Again", icon="⚠️") 
quote=compliment()
st.success(f"🤔 {quote}")

        
