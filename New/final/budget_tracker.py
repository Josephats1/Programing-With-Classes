import csv
from datetime import datetime

def load_transactions(filename):
    """Load financial transactions from CSV file."""
    transactions = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                transactions.append(row)
    except FileNotFoundError:
        print(f"Warning: '{filename}' not found. Starting with empty transactions.")
    return transactions

def save_transactions(filename, transactions):
    """Save transactions to CSV file."""
    with open(filename, 'w', newline='') as file:
        fieldnames = ['date', 'description', 'amount', 'category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

def add_transaction(transactions, description, amount, category):
    """Add a new transaction with current date."""
    transaction = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': amount,
        'category': category
    }
    transactions.append(transaction)
    return transaction

def calculate_balance(transactions):
    """Calculate current balance from all transactions."""
    return sum(t['amount'] for t in transactions)

def get_category_spending(transactions):
    """Return spending by category."""
    categories = {}
    for t in transactions:
        categories[t['category']] = categories.get(t['category'], 0) + t['amount']
    return categories

def generate_report(transactions):
    """Generate financial summary report."""
    balance = calculate_balance(transactions)
    categories = get_category_spending(transactions)
    return {
        'total_transactions': len(transactions),
        'current_balance': balance,
        'categories': categories
    }

def main():
    """Main program interface."""
    filename = "transactions.csv"
    transactions = load_transactions(filename)
    
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Spending by Category")
        print("5. Exit")
        
        choice = input("Select option: ")
        
        if choice == '1':
            desc = input("Income description: ")
            amount = float(input("Amount: "))
            add_transaction(transactions, desc, amount, "Income")
            print("Income recorded!")
            
        elif choice == '2':
            desc = input("Expense description: ")
            amount = -abs(float(input("Amount: ")))  # Ensure negative
            category = input("Category: ")
            add_transaction(transactions, desc, amount, category)
            print("Expense recorded!")
            
        elif choice == '3':
            balance = calculate_balance(transactions)
            print(f"\nCurrent Balance: ${balance:.2f}")
            
        elif choice == '4':
            report = generate_report(transactions)
            print("\nSpending by Category:")
            for cat, amount in report['categories'].items():
                print(f"{cat}: ${amount:.2f}")
                
        elif choice == '5':
            save_transactions(filename, transactions)
            print("Transactions saved. Goodbye!")
            break

if __name__ == "__main__":
    main()