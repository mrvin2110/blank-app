import streamlit as st
import yfinance as yf

# App Title
st.title("SPY 500 ETF Live Performance Tracker")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Live Data", "Historical Chart"])

# Fetch SPY Data
spy = yf.Ticker("SPY")
spy_data = spy.history(period="1d", interval="1m")

if section == "Live Data":
    st.header("Live SPY 500 ETF Data")
    
    # Display latest price
    latest_price = spy_data["Close"].iloc[-1]
    st.metric(label="Current Price", value=f"${latest_price:.2f}")
    
    # Display data table
    st.write("### Latest Trading Data")
    st.dataframe(spy_data.tail(10))
    
elif section == "Historical Chart":
    st.header("SPY 500 ETF Historical Chart")
    
    # Fetch historical data
    hist_data = spy.history(period="1mo")
    
    # Display line chart
    st.line_chart(hist_data["Close"], use_container_width=True)
    
    st.write("### Closing Price Over the Last Month")