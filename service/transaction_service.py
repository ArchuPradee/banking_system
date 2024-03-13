# service/transaction_service.py
import sqlite3
from domain.account import Account

class TransactionService:
    def __init__(self, account_repository):
        self.account_repository = account_repository
        
    def make_transaction(self, account_id, amount, transaction_type):
        # Retrieve the account from the database
        conn = self.account_repository.connection
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY,
                account_id INTEGER,
                amount REAL,
                transaction_type TEXT
            )
        ''')

        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        # Update the account balance based on transaction type
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")

        # Save the updated account balance to the database
        cursor.execute('''
            UPDATE accounts SET balance = ? WHERE account_id = ?
        ''', (account.balance, account_id))
        conn.commit()

        # Record the transaction details
        cursor.execute('''
            INSERT INTO transactions (account_id, amount, transaction_type)
            VALUES (?, ?, ?)
        ''', (account_id, amount, transaction_type))

        return account.balance
