import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2022-03-03"
TODAY = date.today().strftime("%Y-%m-%d")


st.title("Stock Prediction")

stocks = ("AAPL", "GOOG", "MSFT", "AMZN", "FB")
select_stocks = st.selectbox("Select company for prediction", stocks)

n_years = st.slider("Years of prediction:", 1 , 4)
period = n_years * 365

