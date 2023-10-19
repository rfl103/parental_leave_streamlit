import streamlit as st
import pandas as pd

st.set_page_config(page_title="Companies with Best and Worst Leave Policies",
                   layout="wide")

st.title("How much leave does your company offer?")

# Read in Data
parental_leave_data = pd.read_csv("parental_leave.csv")
parental_leave_data = parental_leave_data.fillna(0)

#Removing empty spaces at start of Company value and sorting data by company
parental_leave_data["Company"]=parental_leave_data["Company"].str.strip()
parental_leave_data= parental_leave_data.sort_values(by="Company")

#Adding total leave data
parental_leave_data["Total Maternity Leave"]=parental_leave_data["Paid Maternity Leave"]+parental_leave_data["Unpaid Maternity Leave"]
parental_leave_data["Total Paternity Leave"]=parental_leave_data["Paid Paternity Leave"]+parental_leave_data["Unpaid Paternity Leave"]

# Adding sidebar and company filter
st.sidebar.header("Filter Data Here:")
company = st.sidebar.selectbox(
    "Select the Company:",
    parental_leave_data["Company"].unique()
)

parental_leave_data_selection = parental_leave_data.query(
    'Company == @company'
)
st.image("images/baby.jpg")

st.subheader("Please use the filter to select the company that you are interested in.")

#Metrics

a1,a2,a3 = st.columns(3)
with a1:
    st.metric("Paid Maternity Leave", parental_leave_data_selection["Paid Maternity Leave"])
    st.metric("Paid Paternity Leave", parental_leave_data_selection["Paid Paternity Leave"])

with a2:
    st.metric("Unpaid Maternity Leave", parental_leave_data_selection["Unpaid Maternity Leave"])
    st.metric("Unpaid Paternity Leave", parental_leave_data_selection["Unpaid Paternity Leave"])

with a3:
    st.metric("Total Maternity Leave", parental_leave_data_selection["Total Maternity Leave"])
    st.metric("Total Paternity Leave", parental_leave_data_selection["Total Paternity Leave"])