# expense_system.py
import json
from datetime import datetime

def add_expense(expenses, daily_records):
    """
    Add a new expense with category, amount, and description.
    """
    try:
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        elif len(date) != 10 or date[4] != '-' or date[7] != '-':
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_str = input("Enter amount: ").strip()
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        description = input("Enter description (optional): ").strip()

        # Update category-wise totals
        if category not in expenses:
            expenses[category] = 0.0
        expenses[category] += amount

        # Record daily expense
        record = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        daily_records.append(record)

        print(f"\nExpense added: {amount} under '{category}' on {date}")
        save_data(expenses, daily_records)
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def view_summary(expenses, daily_records):
    """
    Display category-wise totals and export to summary.txt
    """
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n" + "="*50)
    print("EXPENSE SUMMARY")
    print("="*50)
    total = 0
    for category, amount in sorted(expenses.items()):
        print(f"{category:<20}: ${amount:,.2f}")
        total += amount
    print("-" * 50)
    print(f"{'TOTAL':<20}: ${total:,.2f}")
    print("="*50)

    # Export summary to file
    try:
        with open("summary.txt", "w") as f:
            f.write("EXPENSE SUMMARY\n")
            f.write("="*50 + "\n")
            for category, amount in sorted(expenses.items()):
                f.write(f"{category:<20}: ${amount:,.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"{'TOTAL':<20}: ${total:,.2f}\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Summary exported to 'summary.txt'")
    except Exception as e:
        print(f"Error writing summary: {e}")


def export_data(expenses, daily_records):
    """
    Export all daily records to expenses.txt in readable format
    """
    try:
        with open("expenses.txt", "w") as f:
            f.write("DAILY EXPENSE RECORDS\n")
            f.write("="*70 + "\n")
            for record in daily_records:
                desc = record["description"] if record["description"] else "No description"
                f.write(f"Date: {record['date']} | "
                        f"Category: {record['category']:<15} | "
                        f"Amount: ${record['amount']:,.2f} | "
                        f"Description: {desc}\n")
            f.write("\nCATEGORY TOTALS\n")
            f.write("-" * 40 + "\n")
            for cat, amt in sorted(expenses.items()):
                f.write(f"{cat:<20}: ${amt:,.2f}\n")
        print("All data exported to 'expenses.txt'")
    except Exception as e:
        print(f"Error exporting data: {e}")


def save_data(expenses, daily_records):
    """
    Save current state to a JSON file for persistence
    """
    data = {
        "expenses": expenses,
        "daily_records": daily_records
    }
    try:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")


def load_data():
    """
    Load saved data from JSON file
    """
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            return data.get("expenses", {}), data.get("daily_records", [])
    except FileNotFoundError:
        return {}, []
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}, []


def main():
    expenses, daily_records = load_data()
    print("Welcome to Expense Tracker!")

    while True:
        print("\n" + "-"*40)
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Export Data")
        print("4. Exit")
        print("-"*40)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses, daily_records)
        elif choice == "2":
            view_summary(expenses, daily_records)
        elif choice == "3":
            export_data(expenses, daily_records)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()