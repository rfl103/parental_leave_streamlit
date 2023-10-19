import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Parental Leave by Industry",
                   layout="wide")

st.title("Which Industries Offer the Most Leave?")

#parental_leave_data = pd.read_csv("parental_leave.csv")
parental_leave_data = pd.read_csv("parental_leave.csv")
parental_leave_data = parental_leave_data.fillna(0)

#calculating total maternity/paternity leaves
parental_leave_data["Total Maternity Leave"] = parental_leave_data["Paid Maternity Leave"]+parental_leave_data["Unpaid Maternity Leave"]
parental_leave_data["Total Paternity Leave"] = parental_leave_data["Paid Paternity Leave"]+parental_leave_data["Unpaid Paternity Leave"]

#finding industry medians
median_leave_data = parental_leave_data.groupby("Industry")[["Total Maternity Leave", "Total Paternity Leave"]].median().reset_index()

tab1, tab2, tab3 = st.tabs(["Industries that Offer the Most Maternity Leave", "Industries that Offer the Least Maternity Leave",
                      "Industries That Offer the Most Paternity Leave"])

#summary bar chart for top median total maternity
with tab1:
    top_20_median_leave_maternity = median_leave_data.nlargest(n=20, columns=["Total Maternity Leave"], keep="all")
    fig = px.bar(top_20_median_leave_maternity, x="Industry", y=["Total Maternity Leave"],
                 title="Top 20 Industries with Median Highest Weeks of Maternity Leave")
    fig.update_layout(yaxis_title="Total Weeks of Leave")
    st.plotly_chart(fig, use_container_width=True)

#summary bar chart for bottom median total maternity
with tab2:
    bottom_20_median_leave_maternity = median_leave_data.nsmallest(n=20, columns=["Total Maternity Leave"], keep="all")
    fig = px.bar(bottom_20_median_leave_maternity, x="Industry", y=["Total Maternity Leave"],
                 title="20 Industries with Least Median Weeks of Maternity Leave")
    fig.update_layout(yaxis_title="Total Weeks of Leave")
    st.plotly_chart(fig, use_container_width=True)

#summary bar chart for top median paid maternity
with tab3:
    top_20_median_leave_paternity = median_leave_data.nlargest(n=20, columns=["Total Paternity Leave"], keep="all")
    fig = px.bar(top_20_median_leave_paternity, x="Industry", y=["Total Paternity Leave"],
                 title="Top 20 Industries with Median Highest Weeks of Paternity Leave")
    fig.update_layout(yaxis_title="Total Weeks of Leave")
    st.plotly_chart(fig, use_container_width=True)

st.caption("The tabs above show the 20 industries that have the highest/lowest median amounts of maternity leave as well as the highest median amounts of paternity leave.  The 20 industries with the lowest median amounts of paternity leave were not included as these values were all 0.  Disclaimer: more data would be needed to show if this data is representational for each industry as some industries may have a relatively low sample size.")

# SIDEBAR
st.sidebar.header("Filter Data Here:")
industry = st.sidebar.selectbox(
    "Select the Industry:",
    parental_leave_data["Industry"].unique()
)

parental_leave_data_selection = parental_leave_data.query(
    'Industry == @industry'
)

st.write("---")
st.subheader("Please use the filter to select which industry you are interested in.  How many weeks of leave are common in your industry?")


#Median Summary Statistics for overall data set
median_paid_maternity = int(parental_leave_data["Paid Maternity Leave"].median())
median_unpaid_maternity = int(parental_leave_data["Unpaid Maternity Leave"].median())

median_paid_paternity = int(parental_leave_data["Paid Paternity Leave"].median())
median_unpaid_paternity = int(parental_leave_data["Unpaid Paternity Leave"].median())

median_total_maternity = int(parental_leave_data["Total Maternity Leave"].median())
median_total_paternity = int(parental_leave_data["Total Paternity Leave"].median())

#Median Summary Statistics
comp_median_paid_maternity = int(parental_leave_data_selection["Paid Maternity Leave"].median())
comp_median_unpaid_maternity = int(parental_leave_data_selection["Unpaid Maternity Leave"].median())

comp_median_paid_paternity = int(parental_leave_data_selection["Paid Paternity Leave"].median())
comp_median_unpaid_paternity = int(parental_leave_data_selection["Unpaid Paternity Leave"].median())

comp_median_total_maternity = int(parental_leave_data_selection["Total Maternity Leave"].median())
comp_median_total_paternity = int(parental_leave_data_selection["Total Paternity Leave"].median())

a1, a2, a3 = st.columns(3)
with a1:
    st.metric("Median Weeks of Paid Maternity Leave", comp_median_paid_maternity)
    st.metric("Median Weeks of Paid Paternity Leave", comp_median_paid_paternity)
with a2:
    st.metric("Median Weeks of Unpaid Maternity Leave", comp_median_unpaid_maternity)
    st.metric("Median Weeks of Unpaid Paternity Leave", comp_median_unpaid_paternity)
with a3:
    st.metric("Median Weeks ofTotal Maternity Leave", comp_median_total_maternity)
    st.metric("Median Weeks of Total Paternity Leave", comp_median_total_paternity)

b1, b2 = st.columns(2)
with b1:
    #Box Plot for Paid Maternity and Paternity Leave
    fig = px.box(parental_leave_data_selection, y=["Paid Maternity Leave", "Paid Paternity Leave"],
                 title="Paid Maternity and Paternity Leave for Selected Industry")
    st.plotly_chart(fig)

with b2:
    #Box Plot for Total Maternity and Paternity Leave
    fig = px.box(parental_leave_data_selection, y=["Total Maternity Leave", "Total Paternity Leave"],
                 title="Total Maternity and Paternity Leave for Selected Industry")
    st.plotly_chart(fig)






