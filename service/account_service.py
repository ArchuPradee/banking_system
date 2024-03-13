# service/account_service.py
from domain.account import Account
from infra.account_repository import AccountRepository
import sqlite3

class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository
    def create_account(self, customer_id, name, email, phone_number):
        account_number = "ACC123"  # Assume its auto generated
        
        # Create a new account object
        new_account = Account(None, customer_id, account_number, balance=0.0)
        
        # Save the new account to the database
        self.account_repository.save_account(customer_id, name, email, phone_number, new_account)
        
        return new_account
