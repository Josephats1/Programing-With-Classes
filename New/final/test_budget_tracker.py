import pytest
import os
import csv
from budget_tracker import *

@pytest.fixture
def sample_transactions():
    return [
        {'date': '2023-01-01', 'description': 'Salary', 'amount': 2000.0, 'category': 'Income'},
        {'date': '2023-01-02', 'description': 'Rent', 'amount': -1000.0, 'category': 'Housing'}
    ]

def test_load_transactions(tmp_path):
    # Create test CSV
    test_file = tmp_path / "test_transactions.csv"
    with open(test_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'description', 'amount', 'category'])
        writer.writeheader()
        writer.writerow({'date': '2023-01-01', 'description': 'Test', 'amount': '100.0', 'category': 'Test'})
    
    # Test loading
    transactions = load_transactions(test_file)
    assert len(transactions) == 1
    assert transactions[0]['description'] == 'Test'
    assert isinstance(transactions[0]['amount'], float)

def test_add_transaction(sample_transactions):
    original_count = len(sample_transactions)
    new_trans = add_transaction(sample_transactions, "Groceries", -50.0, "Food")
    assert len(sample_transactions) == original_count + 1
    assert new_trans['description'] == "Groceries"
    assert new_trans['amount'] == -50.0

def test_calculate_balance(sample_transactions):
    balance = calculate_balance(sample_transactions)
    assert balance == 1000.0  # 2000 income - 1000 expense

def test_get_category_spending(sample_transactions):
    categories = get_category_spending(sample_transactions)
    assert categories['Income'] == 2000.0
    assert categories['Housing'] == -1000.0

def test_generate_report(sample_transactions):
    report = generate_report(sample_transactions)
    assert report['total_transactions'] == 2
    assert report['current_balance'] == 1000.0
    assert 'Income' in report['categories']