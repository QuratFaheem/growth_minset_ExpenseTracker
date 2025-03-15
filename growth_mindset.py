import csv
import os
import pandas as pd
import streamlit as st
from datetime import datetime

# File to store expenses
file_name = "expenses.csv"

# Ensure CSV file exists
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

# Function to load expenses
def load_expenses():
    return pd.read_csv(file_name)

# Function to add an expense
def add_expense(amount, category, description):
    date = datetime.today().strftime("%Y-%m-%d")
    
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    st.success("✅ Expense added successfully!")

# Function to get total spending
def total_spending(df):
    if df.empty:
        return 0
    return df["Amount"].astype(float).sum()

# Function to get category-wise spending
def category_wise_spending(df):
    if df.empty:
        return pd.DataFrame(columns=["Category", "Amount"])
    return df.groupby("Category")["Amount"].sum().reset_index()

# Streamlit UI
st.title("💰 Simple Expense Tracker")
st.header("Menu")


menu = st.radio("Select an option:", ["Add Expense", "View Expenses", "Total Spending", "Category-wise Spending"])

# Load the expenses data
df = load_expenses()

if menu == "Add Expense":
    st.subheader("📌 Add New Expense")
    
    amount = st.number_input("Enter Amount:", min_value=0.01, step=0.01)
    category = st.selectbox("Select Category:", ["Food", "Travel", "Bills", "Shopping", "Other"])
    description = st.text_input("Enter Description:")
    
    if st.button("Add Expense"):
        if amount and category:
            add_expense(amount, category, description)
        else:
            st.warning("⚠️ Please enter all required fields!")

elif menu == "View Expenses":
    st.subheader("📊 All Expenses")
    if df.empty:
        st.info("No expenses recorded yet.")
    else:
        st.dataframe(df)

elif menu == "Total Spending":
    st.subheader("💸 Total Spending")
    total = total_spending(df)
    st.metric(label="Total Spending", value=f"Rs. {total}")

elif menu == "Category-wise Spending":
    st.subheader("📊 Category-wise Spending")
    category_summary = category_wise_spending(df)
    if category_summary.empty:
        st.info("No expenses recorded yet.")
    else:
        st.dataframe(category_summary)

