import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np
st.set_page_config(page_title="KPI ANALYSIS")

    # Your app code here...
st.title("Welcome to KPI ANALYSIS ")
#function to load the data only once
st.cache_data()
def load_customer_data():
    df = pd.read_excel('datasets/CAR_DATA (2).xlsx',sheet_name=3,skiprows=0)
    return df
with st.spinner("loading dataset"):
    df=load_customer_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show TAX DATASETS"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 
st.subheader('SALES ANALYSIS')

total_mrp_sale=df['Total sale MRP'].sum()
st.metric('Total MRP OF VEHICLE SALES(INCLUDED ASSESORIES MRP PLUS VEHICLE MRP)', f"Rs.{total_mrp_sale}",)

total_acc_sale=df['Total Accessories Sale '].sum()
st.metric('Total MRP OF ACCESSORIES SALES', f"Rs.{total_acc_sale}",)

total_Vehmrp_sale=df['Vehicle MRP '].sum()
st.metric('Total MRP OF VEHICLE(EXCLUDED ASSESORIES SALE)', f"Rs.{total_Vehmrp_sale}",)

st.subheader('PURCHASING  BY DEALER ANALYSIS')
total_mrp_pur=df['NDP(NPP+N Acc P)'].sum()
st.metric('Total MRP OF VEHICLE PURCHASED BY DEALER(INCLUDED ASSESORIES MRP PLUS VEHICLE MRP)', f"Rs.{total_mrp_pur}",)

total_acc_pur=df['N Acc.P'].sum()
st.metric('Total MRP OF ACCESSORIES PURCHASED', f"Rs.{total_acc_pur}",)

total_Vehmrp_PUR=df['N.Purchasing.P'].sum()
st.metric('Total MRP OF VEHICLE PURCHASED BY DEALER(EXCLUDED ASSESORIES PURCHASED COST)', f"Rs.{total_Vehmrp_PUR}",)

st.subheader('PROFIT ANALYSIS')
total_PROFIT=df['PROFIT'].sum()
st.metric('TOTAL PROFIT TO THE DEALER(TOTAL COST OF SALE-TOTAL COST OF PURCHASED)', f"Rs.{total_PROFIT}",)

st.subheader('COMPARISON OF NET DEALER PRICE AND NET SALE PRICE FOR A RESPECTIVE MODEL NAME')
fig1 = px.bar(df, 'CAR ID',['NDP(NPP+N Acc P)','Total sale MRP'],hover_name='Customer Purchase Model Name ', barmode='group')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('COMPARISON OF PROFIT FOR A RESPECTIVE MODEL NAME')
fig1 = px.bar(df, 'CAR ID','PROFIT',hover_name='Customer Purchase Model Name ', barmode='group')
st.plotly_chart(fig1, use_container_width=True)
