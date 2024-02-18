import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

st.write("""
    # Simple Stock Price Prediction App
         Google
""")

st.sidebar.header("User Input Parmeters")

def user_input_features():
    Open=st.sidebar.slider("Open",5.0,20.0,10.0)
    High=st.sidebar.slider("High",5.0,20.0,12.0)
    Low=st.sidebar.slider("Low",5.0,20.0,10.0)

    data={
        "Open": Open,
        "High": High,
        "Low": Low
        }
    
    features=pd.DataFrame(data,index=[0])
    return features

df=user_input_features()

st.subheader("User Input Features")
st.write(df)

#training data
tickerSysmbol='GOOGL'

tickerData= yf.Ticker(tickerSysmbol)

ticker_df=tickerData.history(period='1d',start='2010-5-31', end='2020-5-31')

st.subheader("Stock Price Data")
st.write(ticker_df) #ticker_df is pandas Dataframe

#Linear Regression
X=ticker_df[['Open','High','Low']]
Y=ticker_df['Close']

model=LinearRegression()
model.fit(X,Y)

prediction=model.predict(df)

st.subheader("Prediction")
st.write(prediction)







