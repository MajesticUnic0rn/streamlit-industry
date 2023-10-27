# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page Config
st.set_page_config(page_title="Marketing Dashboard", page_icon="📉")
st.sidebar.header("Marketing Dashboard")

# Streamlit Marketing Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Mock Data Generation
date_range = pd.date_range(start="2022-01-01", end="2022-12-31", freq="M")

# Lead conversion data
leads = np.random.randint(1000, 5000, len(date_range))
conversions = np.random.randint(300, 1200, len(date_range))
conversion_rate = conversions/leads * 100
leads_data = pd.DataFrame({
    'Date': date_range,
    'Leads': leads,
    'Conversions': conversions,
    'Conversion Rate': conversion_rate
})

# Social media audience data
platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn", "TikTok"]
audiences = np.random.randint(5000, 50000, size=(len(platforms)))
audience_data = pd.DataFrame({
    'Platform': platforms,
    'Audience': audiences
})

# Streamlit app
st.title("Marketing Industry Dashboard")

# KPI Metrics
st.header("KPI Metrics Overview")
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(label="Total Leads (2022)", value="{:,.0f}".format(leads_data['Leads'].sum()))
with kpi2:
    st.metric(label="Total Conversions (2022)", value="{:,.0f}".format(leads_data['Conversions'].sum()))
with kpi3:
    st.metric(label="Average Conversion Rate", value="{:,.2f}%".format(leads_data['Conversion Rate'].mean()))

# Charts
st.header("Lead Conversion Overview")
fig1 = px.line(leads_data, x='Date', y=['Leads', 'Conversions'], title="Monthly Leads and Conversions (2022)")
st.plotly_chart(fig1)

fig2 = px.bar(audience_data, x='Platform', y='Audience', title="Social Media Target Audience", color='Platform')
st.plotly_chart(fig2)

st.write("Note: All data presented here is mock data and for demonstration purposes only.")

# Run this script to see the Streamlit dashboard for the marketing industry.
