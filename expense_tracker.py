import csv
import datetime
import os

# File to store expenses
default_file = 'expenses.csv'

# Initialize CSV file with header if not exists
def init_file(file_name= default_file):
    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'category', 'amount', 'description'])


# Add a new expense record
def add_expense(date_str, category, amount, description, file_name=default_file):
    with open(file_name, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([date_str, category, amount, description])
    print(f"Added: {date_str} | {category} | {amount} | {description}")


# View all expenses
def view_expenses(file_name=default_file):
    print("\nAll Expenses:")
    print("Date       | Category    | Amount    | Description")
    print("-"*60)
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['date']} | {row['category']:<11} | {row['amount']:<8} | {row['description']}")
    print()


# View summary by category
def view_summary(file_name=default_file):
    summary = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row['category']
            amt = float(row['amount'])
            summary[cat] = summary.get(cat, 0) + amt

    print("\nExpense Summary by Category:")
    for cat, total in summary.items():
        print(f"{cat:<15}: {total}")
    print()


# Main menu loop
def main():
    init_file()
    while True:
        print("Choose an option:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")
        choice = input("Select (1-4): ")

        if choice == '1':
            date_input = input("Enter date (YYYY-MM-DD) [default today]: ") or datetime.date.today().isoformat()
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(date_input, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()