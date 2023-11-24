import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np
# change plotly theme
#the set_page_config function is used to customize
#the configuration of your app's page. 
st.set_page_config(page_title="SALES PERFORMANCE AND DASHBOARD")

    # Your app code here...
st.title("Welcome to CAR'S SALES PERFORMANCE AND DASHBOARD ")
st.write("#####This is a sales performance dashboard app#####")

st.title('About Sales Performance Dashboard')
st.image('images/car1.png')
st.info(''' A sales performance dashboard is a visual representation of key sales metrics and performance indicators, typically presented in a graphical format. It provides a concise and easy-to-understand overview of the sales team's performance, allowing managers and stakeholders to quickly assess progress and identify areas that need improvement. Sales performance dashboards are commonly used in various industries, including car dealerships, to track and optimize sales efforts.

In the context of a car dealership, a sales performance dashboard would include data and metrics related to the sales of vehicles and associated activities. Some of the key components and metrics typically found in a car dealership's sales performance dashboard may include:

Vehicle Sales: The total number of cars sold during a specific period, which could be daily, monthly, quarterly, or yearly.

Revenue and Profit: The total revenue generated from vehicle sales and the associated profit margins. ##### helps to gauge the financial health of the dealership.

Salesperson Performance: Individual salesperson metrics, such as the number of cars sold, revenue generated, conversion rates, and customer satisfaction scores. ##### allows managers to identify top-performing salespeople and those who may need additional support or training.

Lead Conversion Rate: The percentage of leads that result in actual car sales. ##### metric helps evaluate the efficiency of the sales team in converting potential customers into buyers.

Inventory Turnover: How quickly the dealership's inventory of cars is being sold and replaced with new vehicles. A high inventory turnover rate indicates efficient sales operations.

Average Selling Price: The average price at which cars are sold. ##### metric is essential for pricing strategies and understanding customer preferences.

Sales by Vehicle Model: A breakdown of sales performance by different car models. ##### information can guide inventory management and marketing efforts.

''')

st.title('Sales Performance Dashboard Significance')
st.info(''' The significance of a sales performance dashboard in a car dealership lies in its ability to provide real-time insights into the sales team's performance and the overall health of the business. By having access to these data-driven insights, car dealership managers can make informed decisions, set realistic sales targets, implement effective sales strategies, and identify areas where additional support or training is needed.

Moreover, a well-designed dashboard fosters transparency and healthy competition among sales team members, as everyone can see their individual and team performance metrics. ##### can motivate the sales staff to strive for better results, leading to increased sales and improved customer satisfaction.

In summary, a sales performance dashboard is a powerful tool for car dealerships to monitor their sales performance, optimize operations, and achieve their business goals.
''')
st.title('Key Components of the sales performance and dashboard')
st.info('''A sales performance dashboard for the automobile sector typically includes key metrics and components that provide insights into various aspects of the sales process. Here are some key components you might consider for a sales performance dashboard in the automobile sector:

Sales Overview-->

Total Sales: A summary of total sales over a specific period.
Sales Growth: Percentage increase or decrease in sales compared to a previous period.

Unit Sales-->
        
New Car Sales: Number of new cars sold.
        
Used Car Sales: Number of used cars sold.

Sales by Model: Breakdown of sales by specific car models.
        
Revenue Metrics-->

Total Revenue: Overall revenue generated from sales.

Average Revenue per Sale: Average revenue generated per unit sold.

Customer Demographics-->

Buyer Age Group: Distribution of buyers based on age.
        
Gender Distribution: Percentage of male and female buyers.

Profitability Metrics-->

Gross Profit Margin: Percentage difference between revenue and cost of goods sold.
        
Net Profit: Overall profitability after considering all expenses.

Customer Satisfaction-->

Post-Sale Surveys: Feedback from customers on their satisfaction.
        
Customer Retention Rate: Percentage of customers retained over a specific period.

Financial KPIs-->

Return on Investment (ROI): Measurement of the profitability of sales efforts.
        
Cost per Acquisition (CPA): The cost associated with acquiring a new customer.

Forecasting-->
        
Sales Forecast: Predictions for future sales based on historical data and market trends.

''')