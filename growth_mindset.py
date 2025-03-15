import csv
import os
import pandas as pd
from datetime import datetime


file_name="expenses.csv"

if not os.path.exists(file_name):
    with open(file_name,"w",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Amount','Category','Description'])

def add_expense():
    date=datetime.today().strftime('%Y-%m-%d')
    amount=input("Enter the amount: ")
    category=input("Enter the category: (Food, Travel, Rent, Bills, Others) ")
    description=input("Enter the description: ")

    with open(file_name,"a",newline='') as file:
        writer=csv.writer(file)
        writer.writerow([date,amount,category,description])

        print("✅Expense added successfully")


def view_expenses():
    df=pd.read_csv(file_name)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)

def total_spending():
    df= pd.read_csv(file_name)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        total=df["Amount"].astype(float).sum()
        print(f"💰Total spending: ${total}")

def category_wise_spending():
    df = pd.read_csv(file_name)
    if df.empty:
        print("No expenses recorded yet.")
    else:
        category_sum = df.groupby("Category")["Amount"].sum()  # Group by category and sum amounts
        print(category_sum)

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            category_wise_spending()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
