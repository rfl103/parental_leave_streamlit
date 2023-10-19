import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

st.set_page_config(page_title="Company Parental Leave Policies",
                   page_icon=":man_feeding_baby:",
                   layout="wide")

# Read in Data
parental_leave_data = pd.read_csv("parental_leave.csv")
parental_leave_data["Total Maternity Leave"]=parental_leave_data["Paid Maternity Leave"]+parental_leave_data["Unpaid Maternity Leave"]
parental_leave_data["Total Paternity Leave"]=parental_leave_data["Paid Paternity Leave"]+parental_leave_data["Unpaid Paternity Leave"]

st.markdown("<h1 style='text-align: center; color: black;'>Parental Leave Policies </h1>", unsafe_allow_html=True)

st.write("In the United States, there are no federal guidelines that dictate pair parental leave."
         "While many parents do receive some amount of leave through the Family Medical Leave Act, it is not always paid "
         "and not all workers qualify.  This analysis will explore what the average amounts of leave are, what is the typical "
         "leave policy of each industry, and leave policies reported for various companies.")

st.subheader("How many weeks of leave does the average employee get?")
a1,a2 = st.columns(2)
with a1:
    fig = px.histogram(parental_leave_data, x = "Paid Maternity Leave", color_discrete_sequence=["blue"], opacity= 0.5, nbins=50, marginal="box",
                        title="Paid Maternity and Paternity Leave Distribution")
    fig.add_trace(px.histogram(parental_leave_data, x='Paid Paternity Leave', color_discrete_sequence=['red'], opacity=0.5, nbins=50).data[0])
    fig.update_layout(barmode="overlay")
    fig.update_xaxes(title_text="Weeks of Paid Leave")
    st.plotly_chart(fig)

with a2:
    fig = px.histogram(parental_leave_data, x = "Total Maternity Leave", color_discrete_sequence=["blue"], opacity= 0.5, nbins=50, marginal="box",
                        title="Total Maternity and Paternity Leave Distribution")
    fig.add_trace(px.histogram(parental_leave_data, x='Total Paternity Leave', color_discrete_sequence=['red'], opacity=0.5, nbins=50).data[0])
    fig.update_layout(barmode="overlay")
    fig.update_xaxes(title_text="Total Weeks of Leave")
    st.plotly_chart(fig)

st.caption("The distribution plots above show how weeks of leave are distributed across companies.  Maternity leave is shown in blue and paternity leave is shown in maroon with the amount paid on the left and the total amount on the right.  It is apparent that it is much more common for a company to offer maternity leave than paternity leave.")
st.subheader("Key Metrics")

#Median Summary Statistics
median_paid_maternity = int(parental_leave_data["Paid Maternity Leave"].median())
median_unpaid_maternity = int(parental_leave_data["Unpaid Maternity Leave"].median())

median_paid_paternity = int(parental_leave_data["Paid Paternity Leave"].median())
median_unpaid_paternity = int(parental_leave_data["Unpaid Paternity Leave"].median())

median_total_maternity = int(parental_leave_data["Total Maternity Leave"].median())
median_total_paternity = int(parental_leave_data["Total Paternity Leave"].median())

b1, b2, b3 = st.columns(3)
with b1:
    st.metric("Median Weeks of Paid Maternity Leave", median_paid_maternity)
    st.metric("Median Weeks of Paid Paternity Leave", median_paid_paternity)
with b2:
    st.metric("Median Weeks of Unpaid Maternity Leave", median_unpaid_maternity)
    st.metric("Median Weeks of Unpaid Paternity Leave", median_unpaid_paternity)
with b3:
    st.metric("Median Weeks ofTotal Maternity Leave", median_total_maternity)
    st.metric("Median Weeks of Total Paternity Leave", median_total_paternity)

st.subheader("Do companies that offer more weeks of maternity leave tend to offer more weeks of paternity leave?")

c1,c2=st.columns(2)
with c1:
    fig = px.scatter(parental_leave_data, x="Paid Maternity Leave", y="Paid Paternity Leave", trendline="ols", title="Paid Maternity Leave vs Paid Paternity Leave")
    st.plotly_chart(fig)
with c2:
    fig = px.scatter(parental_leave_data, x="Total Maternity Leave", y="Total Paternity Leave", trendline="ols",
                     title="Total Maternity Leave vs Total Paternity Leave")
    st.plotly_chart(fig)

st.caption("It does appear that there is a correlation between companies that offer maternity leave and paternity leave.")


