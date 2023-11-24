import streamlit as st 
import pandas as pd 
import plotly.express as px
import numpy as np
# change plotly theme
#the set_page_config function is used to customize
#the configuration of your app's page. 
st.set_page_config(page_title="CARS STOCK ANALYSIS")

    # Your app code here...
st.title("CARS STOCK INVENTORY ANALYSIS ")
#function to load the data only once
st.cache_data()
def load_data():
    df = pd.read_excel('datasets/CAR_DATA (2).xlsx',sheet_name=1,skiprows=2)
    return df
with st.spinner("loading dataset"):
    df=load_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show Car's Datasets"):
    st.subheader('📅 Raw datasets')
    st.dataframe(df) 

total_vehicle=df['Total Vehicle Retail '].sum()
st.metric('Total Number of Vehicles Retail:', f"{total_vehicle}",)

total_vehicl=df['Total Vehicle Wholesale '].sum()
st.metric('Total Number of Vehicles Wholesale:', f"{total_vehicl}",)

total_vehic=df['DEADSTOCK'].sum()
st.metric('Total Number of Deadstock:', f"{total_vehic}",)

st.subheader('No.of vehicles wholesale in a year')
result_df =df.groupby('Month ')['Total Vehicle Wholesale '].sum().reset_index()
fig1 = px.bar(result_df, 'Month ','Total Vehicle Wholesale ')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('No.of vehicles retail in a year')
resul_df =df.groupby('Month ')['Total Vehicle Retail '].sum().reset_index()
fig1 = px.bar(resul_df, 'Month ','Total Vehicle Retail ')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('Analysis of wholesale and retail sale:')
fig2 = px.bar(df, 'Month ',['Total Vehicle Wholesale ','Total Vehicle Retail '],hover_name='Wholesale Vehicle Model Name ', barmode='group')
st.plotly_chart(fig2, use_container_width=True)
