from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category, date):
        self.expenses.append({'amount': amount, 'description': description, 'category': category, 'date': date})

    def get_monthly_summary(self, month, year):
        total_expenses = 0
        for expense in self.expenses:
            if expense['date'].month == month and expense['date'].year == year:
                total_expenses += expense['amount']
        return total_expenses

    def get_category_expense(self, category):
        category_expense = 0
        for expense in self.expenses:
            if expense['category'] == category:
                category_expense += expense['amount']
        return category_expense

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("Expenses:")
            for expense in self.expenses:
                print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")

# Sample usage
foodexpen = int(input("Enter food expense: "))
travelexpen = int(input("Enter transportation expense: "))
entertainmentexpen = int(input("Enter entertainment expense: "))

tracker = ExpenseTracker()

# Adding expenses
tracker.add_expense(foodexpen, "Groceries", "Food", datetime(2024, 2, 5))
tracker.add_expense(travelexpen, "Transportation", "Travel", datetime(2024, 2, 6))
tracker.add_expense(entertainmentexpen, "Movie tickets", "Entertainment", datetime(2024, 2, 7))

# Viewing expenses
tracker.view_expenses()

# Getting monthly summary
total_monthly_expenses = tracker.get_monthly_summary(2, 2024)  # Assuming February 2024
print(f"Total monthly expenses: {total_monthly_expenses}")

# Getting category-wise expense
food_expense = tracker.get_category_expense("Food")
print(f"Food expenses: {food_expense}")
