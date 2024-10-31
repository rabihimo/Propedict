import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go
import appdirs as ad
import yfinance as yf
import pandas as pd

# Remove the unnecessary pip installs within the script
# !pip -q install streamlit #-q install quietly
# !pip install appdirs

# Correct the appdirs usage
# ad.user_cache_dir = lambda *args: "/tmp"  # This line is likely unnecessary and might cause issues

# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input")
symbol = st.sidebar.text_input('Please enter the stock symbol: ', 'NVDA').upper()
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2024,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())

st.title(f"{symbol}")

try:
    stock = yf.Ticker(symbol)
    # Display company's basics
    st.write(f"# Sector : {stock.info['sector']}")
    st.write(f"# Company Beta : {stock.info['beta']}")

    data = yf.download(symbol,start=sdate,end=edate)
    if data.empty:
        st.error(f"No data found for symbol '{symbol}' within the specified date range.")
    else:
      st.line_chart(data['Close'],x_label="Date",y_label="Close")
except Exception as e:
    st.error(f"An error occurred: {e}")

