# service/statement_service.py
import sqlite3

class StatementService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        statement = f"Account statement for Account ID: {account.account_id}\n"
        statement += f"Customer ID: {account.customer_id}\n"
        statement += f"Account Number: {account.account_number}\n"
        statement += f"Balance: {account.get_balance()}\n\n"

        statement += "Transaction History:\n"
        transactions = self._get_transaction_history(account_id)
        for transaction in transactions:
            statement += f"Transaction ID: {transaction['transaction_id']}, Amount: {transaction['amount']}, Transaction_Type: {transaction['transaction_type']}\n"

        return statement

    def _get_transaction_history(self, account_id):
        connection = self.account_repository.connection  # Create a new connection to in-memory SQLite database
        cursor = connection.cursor()
        cursor.execute('''
            SELECT transaction_id, amount, transaction_type
            FROM transactions
            WHERE account_id = ?
        ''', (account_id,))
        transactions = cursor.fetchall()
        return [{"transaction_id": row[0], "amount": row[1], "transaction_type": row[2]} for row in transactions]

    # Rest of the class implementation...
