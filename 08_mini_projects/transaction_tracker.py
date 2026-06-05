"""
Topic   : Mini Project — Daily Transaction Tracker
Date    : December 16, 2025
Author  : Chaitanya

Description : A simple CLI tool to log daily financial transactions
              (credit/debit) with category, payment method and notes.
"""

from datetime import date


def record_transaction():
    """Record a single financial transaction with all relevant details."""
    day = date.today()

    amount = float(input("Enter amount you want to log: "))
    category = input("Enter the amount category (Credit/Debit): ")
    payment_method = str.capitalize(input("Enter the payment method (CASH/UPI): "))
    description = str.capitalize(input("Enter note if you want to add: "))

    if description == "":
        description = "Hey, I need to make a log of my money."

    print("\nFollowing is the daily log of your transaction:")
    print(f"Created on {day}")
    print(f"Amount: {amount} | Category: {category} | Method: {payment_method}")
    print(f"Description:\n{description}")


if __name__ == "__main__":
    record_transaction()
