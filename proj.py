import os
import datetime

# Function to display the menu
def display_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

# Function to add an expense
def add_expense():
    amount = float(input("Enter the expense amount: "))
    description = input("Enter a brief description: ")

    # Get the current date and time
    date_time = datetime.datetime.now()
    date = date_time.strftime("%Y-%m-%d %H:%M:%S")

    # Append the expense details to the text file
    with open("expenses.txt", "a") as file:
        file.write(f"{date} - {amount:.2f} - {description}\n")

    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if expenses:
            print("Date                | Amount  | Description")
            print("-------------------------------------------")
            for expense in expenses:
                print(expense.strip())
        else:
            print("No expenses recorded.")
    except FileNotFoundError:
        print("No expenses recorded.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting the expense tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
