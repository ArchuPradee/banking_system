# infra/account_repository.py
import sqlite3
from domain.account import Account

class AccountRepository:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')

    def save_account(self, customer_id, name, email, phone_number, account):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone_number TEXT
            )
        ''')
        cursor.execute('''
            INSERT INTO customer (customer_id, name, email, phone_number)
            VALUES (?, ?, ?, ?)
        ''', (customer_id,name, email, phone_number))
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                account_number TEXT,
                balance REAL
            )
        ''')
        cursor.execute('''
            INSERT INTO accounts (customer_id, account_number, balance)
            VALUES (?, ?, ?)
        ''', (customer_id, account.account_number, account.balance))
        account.account_id = cursor.lastrowid
        self.connection.commit()
        return account.account_id

    def find_account_by_id(self, account_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT account_id, customer_id, account_number, balance
            FROM accounts
            WHERE account_id = ?
        ''', (account_id,))
        account_data = cursor.fetchone()
        if account_data:
            return Account(*account_data)
        else:
            return None

    def find_accounts_by_customer_id(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT account_id, customer_id, account_number, balance
            FROM accounts
            WHERE customer_id = ?
        ''', (customer_id,))
        accounts_data = cursor.fetchall()
        return [Account(*account_data) for account_data in accounts_data]
