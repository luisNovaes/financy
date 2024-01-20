import streamlit as st
import yfinance as yf
from datetime import datetime
import pandas as pd

df = pd.read_csv("data/bats_symbols.csv")
simbols = df['Name'].unique()

import streamlit as st

st.markdown("""
<style>
    [data-testid=stTable] {
        background-color: #f2f1d0;
        
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    "# Financial Market"
    selected = st.selectbox('Select Ticket',  df['Name'].unique().tolist())
    start_date = st.date_input("Insert start date").strftime('%Y-%m-%d')
    end_date = st.date_input("Insert end date").strftime('%Y-%m-%d')

st.title(':blue[Financial Market] :sunglasses:')
st.subheader("Stocks "  + selected)

if st.sidebar.button("Get Quote"):
    amzn = yf.Ticker(selected)
    amzn_hist = amzn.history(start=start_date, end=end_date)
    st.table(amzn_hist[["Open","High","Low","Close","Volume"]])

st.sidebar.markdown("###### By luismagnovaes@gmail.com")






