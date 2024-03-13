# tests/test_transaction_service.py
import unittest
from infra.account_repository import AccountRepository
from service.account_service import AccountService
from service.transaction_service import TransactionService

class TestTransactionService(unittest.TestCase):
    def setUp(self):
        self.account_repository = AccountRepository()
        acc_service = AccountService(self.account_repository)
        self.transaction_service = TransactionService(self.account_repository)
        self.account = acc_service.create_account(1, 'Demo', 'demo@gmail.com', '978675')

    def test_deposit_transaction(self):
        amount = self.transaction_service.make_transaction(self.account.account_id, 100, 'deposit')
        self.assertEqual(amount, 100.0)
    
    def test_withdraw_transaction(self):
        self.transaction_service.make_transaction(self.account.account_id, 100, 'deposit')
        amount = self.transaction_service.make_transaction(self.account.account_id, 50, 'withdraw')
        self.assertEqual(amount, 50.0)
        
    def test_account_balance(self):
        self.transaction_service.make_transaction(self.account.account_id, 100, 'deposit')
        account = self.account_repository.find_account_by_id(self.account.account_id)
        balance = account.get_balance()
        self.assertEqual(balance, 100.0)
        
    def test_insufficient_balance_to_withdraw(self):
        self.transaction_service.make_transaction(self.account.account_id, 100, 'deposit')
        self.transaction_service.make_transaction(self.account.account_id, 50, 'withdraw')
        with self.assertRaises(ValueError):
            self.transaction_service.make_transaction(self.account.account_id, 100, 'withdraw')
    


if __name__ == '__main__':
    unittest.main()
