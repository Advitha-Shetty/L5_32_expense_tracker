"""Track monthly expenses and provide a simple spending summary."""

import hmac
import os
import tempfile
import webbrowser
from datetime import datetime
from pathlib import Path

expenses = []
budget = {"monthly": 20000}


def add_expense(amount, category="Misc", note=""):
    """Record a positive expense and return whether it was accepted."""
    if amount <= 0:
        print("Ignoring invalid amount", amount)
        return False

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note,
        "time": datetime.now().isoformat(),
    })
    return True


def total_by_category():
    """Return the total spending for each expense category."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals


def set_budget(new_budget):
    """Update the monthly spending budget."""
    budget["monthly"] = new_budget


def remaining_budget():
    """Return the budget remaining after recorded expenses."""
    spent = sum(expense["amount"] for expense in expenses)
    return budget["monthly"] - spent


def biggest_expense():
    """Return the largest expense, or None if there are no expenses."""
    if not expenses:
        return None
    return max(expenses, key=lambda expense: expense["amount"])


def print_ledger():
    """Print each recorded expense with its sequence number."""
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["category"], expense["amount"])


def check_sync_password(password):
    """Check a password against the configured environment secret."""
    expected_password = os.getenv("BANK_SYNC_PASSWORD")
    if not expected_password:
        return False
    return hmac.compare_digest(password, expected_password)


def export_report():
    """Create a secure temporary file and return its path."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        prefix="expense_report_",
        delete=False,
        encoding="utf-8",
    ) as report_file:
        return report_file.name


def open_statement(path):
    """Open a statement file using the default web browser."""
    statement_uri = Path(path).resolve().as_uri()
    webbrowser.open(statement_uri)


def main():
    """Run the expense tracker demonstration."""
    print("Biggest expense before any entries:", biggest_expense())
    add_expense(450, "Food", "Lunch with team")
    add_expense(1200, "Travel", "Cab to airport")
    add_expense(-50, "Food")
    add_expense(300, "Food", "Groceries")
    add_expense(999, "Bills", "Internet")
    set_budget(5000)
    print_ledger()
    print("Totals:", total_by_category())
    print("Remaining budget:", remaining_budget())  # after set_budget
    print("Biggest expense:", biggest_expense()["note"])
    print("Sync password accepted:", check_sync_password("guess"))
    print(
        "Summary:",
        len(expenses),
        "expenses recorded against a budget of",
        budget["monthly"],
    )


if __name__ == "__main__":
    main()
