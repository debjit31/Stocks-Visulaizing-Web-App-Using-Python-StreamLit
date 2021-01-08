import yfinance as yf
import streamlit as st
import pandas as pd


stock_ticker = {'Google' : 'GOOGL',
            'Apple Inc.' : 'AAPL',
            'Microsoft' : 'MSFT',
            'Facebook' : 'FB',
            'Amazon' : 'AMZN',
            'Netflix Inc.' : 'NFLX'}

st.write("""
    # Select a Stock to Visualize!
    """)

option = st.selectbox('',
    ('Google', 'Apple Inc.', 'Facebook', 'Microsoft', 'Amazon', 'Netflix Inc.'))

st.write("""
    #   Simple Stock Price App

    ##  Shown are the stock closing price and volume of %s!

    """ %(option))

tickerSymbol = stock_ticker[option]
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end = '2020-5-31')
col1, col2 = st.beta_columns(2)
with col1:
    st.write("""
        ## Opening Prices
        """)
    st.line_chart(tickerDf.Open)
    st.write("""
        ## Closing Prices
        """)
    st.line_chart(tickerDf.Close)
    st.write("""
        ## Volume Prices
        """)
    st.line_chart(tickerDf.Volume)
with col2:
    st.write("""
        ## High Prices
        """)
    st.line_chart(tickerDf.High)
    st.write("""
        ## Low Prices
        """)
    st.line_chart(tickerDf.Low)
    st.write("""
        ## Dividends
        """)
    st.line_chart(tickerDf.Dividends)

