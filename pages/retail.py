# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page Config
st.set_page_config(page_title="Retail Dashboard", page_icon="📉")
st.markdown("# Retail Dashboard")
st.sidebar.header("Retail Dashboard")

# Generate mock data
date_range = pd.date_range(start="2022-01-01", end="2022-12-31", freq="M")
sales_data = pd.DataFrame({
    'Date': date_range,
    'Sales': np.random.rand(len(date_range)) * 1000
})

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
product_sales = np.random.randint(50, 200, size=(len(date_range), len(products)))
product_sales_data = pd.DataFrame(product_sales, columns=products, index=date_range).reset_index().melt(id_vars='index', value_vars=products, var_name='Product', value_name='Units Sold')

inventory_data = pd.DataFrame({
    'Date': date_range,
    'Inventory Level': np.cumsum(np.random.randint(-20, 50, len(date_range)))
})

customer_ages = ["20s", "30s", "40s", "50s", "60s"]
customer_data = pd.DataFrame({
    'Age Group': customer_ages,
    'Count': np.random.randint(100, 1000, len(customer_ages))
})

# Mock Deltas (You should replace these with real calculations from your data)
sales_delta = sales_data['Sales'].iloc[-1] - sales_data['Sales'].iloc[-2]
avg_sales_delta = sales_data['Sales'].mean() - sales_data['Sales'].shift(1).mean()
product_sales_delta = product_sales_data['Units Sold'].sum() - product_sales_data['Units Sold'].shift(1).sum()
inventory_delta = inventory_data['Inventory Level'].iloc[-1] - inventory_data['Inventory Level'].iloc[-2]

# Streamlit app
st.title("Retail Industry Dashboard")

# KPI metrics overview
st.header("KPI Metrics Overview")

# Using columns to display metrics in a grid layout
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(label="Total Sales (2022)", value="${:,.2f}".format(sales_data['Sales'].sum()), delta="{:,.2f}".format(sales_delta))
with kpi2:
    st.metric(label="Average Monthly Sales", value="${:,.2f}".format(sales_data['Sales'].mean()), delta="{:,.2f}".format(avg_sales_delta))
with kpi3:
    st.metric(label="Total Products Sold", value="{:,.0f}".format(product_sales_data['Units Sold'].sum()), delta="{:,.0f}".format(product_sales_delta))
with kpi4:
    st.metric(label="Active Inventory Level", value="{:,.0f}".format(inventory_data['Inventory Level'].iloc[-1]), delta="{:,.0f}".format(inventory_delta))

# Sales overview
st.header("Sales Overview")

# Using columns to create a grid layout
col1, col2 = st.columns(2)

with col1:
    fig1 = px.line(sales_data, x='Date', y='Sales', title="Monthly Sales (2022)")
    st.plotly_chart(fig1)

fig2 = px.bar(product_sales_data.groupby('Product')['Units Sold'].sum().reset_index(), x='Product', y='Units Sold', title="Top Products by Sales (2022)")
st.plotly_chart(fig2)

# Inventory analysis
st.header("Inventory Analysis")
fig3 = px.line(inventory_data, x='Date', y='Inventory Level', title="Inventory Levels (2022)")
st.plotly_chart(fig3)

# Customer analysis
st.header("Customer Analysis")
fig4 = px.bar(customer_data, x='Age Group', y='Count', title="Customer Demographics by Age", color='Age Group', color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig4)

if __name__ == "__main__":
    pass
