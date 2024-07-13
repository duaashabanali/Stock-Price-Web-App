import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
 # Simple Stock Price App
         
Enter stock market ticker in the box below to get its **closing price** and **volume** charts respectivly!
         
""")
tickerSymbol = st.text_input("Stock market ticker")
# tickerSymbol = "googl"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)