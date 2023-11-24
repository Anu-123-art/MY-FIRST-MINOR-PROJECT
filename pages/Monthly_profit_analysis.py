import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np
st.set_page_config(page_title="MONTHWISE PROFIT ANALYSIS")

    # Your app code here...
st.title("MONTHWISE PROFIT ANALYSIS ")
#function to load the data only once
st.cache_data()
def load_customer_data():
    df = pd.read_excel('datasets/CAR_DATA (2).xlsx',sheet_name=4,skiprows=0)
    return df
with st.spinner("loading dataset"):
    df=load_customer_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("PROFIT ANALYSIS BY MONTH"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 

st.subheader('TOTAL MONTHWISE SALE:')
fig1 = px.pie(df, 'MONTH', 'TOTAL MONTH WISE SALE')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('COMPARISON OF TOTAL MONTH WISE SALE AND NDP')
fig1 = px.bar(df, 'MONTH',['TOTAL MONTH WISE NDP','TOTAL MONTH WISE SALE'],barmode='group' )
st.plotly_chart(fig1, use_container_width=True)


st.subheader('TOTAL MONTH WISE PROFIT:')
fig3 = px.pie(df, 'MONTH', 'TOTAL MONTH WISE PROfit')
st.plotly_chart(fig3, use_container_width=True)



