import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme
#the set_page_config function is used to customize
#the configuration of your app's page. 
st.set_page_config(page_title="CARS DETAILS")

    # Your app code here...
st.title("Welcome to CAR'S DETAILS ")
st.image('images/car15.jpg')
#function to load the data only once
st.sidebar.title("DATASETS CONTENT")
st.cache_data()
def load_spend_data():
    df = pd.read_excel('datasets/CAR_DATA (2).xlsx',skiprows=2)
    return df
with st.spinner("loading dataset"):
    df=load_spend_data()
st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show Car's Datasets"):
    st.subheader('📅 CAR DETAILS DATASETS')
    st.dataframe(df) 
if st.sidebar.checkbox("Count of fuel type vehicle"):
    st.subheader('Analysis on fuel type vehicle')
    vehicle_fuel=df['Fuel Type '].value_counts()
    chart1 = px.pie(vehicle_fuel,vehicle_fuel.index,vehicle_fuel.values)
    st.plotly_chart(chart1, use_container_width=True)


st.subheader('VALUE COUNT OF MODEL NAME')
models = df['Model Name '].value_counts()
fig2 = px.funnel(models, models.index, models.values)
st.plotly_chart(fig2, use_container_width=True)

st.subheader('ANALYSIS OF ON ROAD PRICE WITH ITS MODEL NAME')
fig1 = px.area(df, 'Model Name ', 'On road Price ')
st.plotly_chart(fig1, use_container_width=True)
st.write("This graph shows the analysis of on road price with its model name.It help customer to compare and get a good car within its budget. ")

st.subheader('SHOWING COMPARISON OF ON ROAD PRICE AND EX SHOWROOM PRICE FOR ITS RESPECTIVE MODELS')
fig2 = px.bar(df, 'CAR ID',['On road Price ','Ex Showroom Price '],hover_name='Model Name ', barmode='group')
st.plotly_chart(fig2, use_container_width=True)
st.write("This bar graph shows the comaprison of on roadprice(which include all the tax) and ex showroom price(which exclude all the tax).This give customer brief information about how much he/she is getting profit for a respective model.")

st.subheader('SHOWING ANALYSIS OF ON ROAD PRICE FOR A VARIENTS FOR ITS RESPECTIVE MODELS')
fig4 = px.bar(df, 'Varient ','On road Price ',hover_name='Model Name ', barmode='group')
st.plotly_chart(fig4, use_container_width=True)
st.write("THis graph shows analysis of on road price for a varients for its repective models.")

st.subheader('SHOWING COMPARISON OF ON ROAD PRICE AND EX SHOWROOM PRICE FOR A VARIENTS FOR ITS RESPECTIVE MODELS')
fig3 = px.bar(df, 'Varient ',['On road Price ','Ex Showroom Price '],hover_name='Model Name ', barmode='group')
st.plotly_chart(fig3, use_container_width=True)
st.write("This graph show the comparison of on road and ex showroom price for a varients associated with repsective models. This help customer to analyis the price on varient basis to. ")




