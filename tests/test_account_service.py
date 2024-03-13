# tests/test_account_service.py
import unittest
from service.account_service import AccountService
from infra.account_repository import AccountRepository

class TestAccountService(unittest.TestCase):
    def setUp(self):
        acc_repo = AccountRepository()
        self.account_service = AccountService(acc_repo)

    # Add test methods here
    def test_create_account(self):
        # Create an account
        acc = self.account_service.create_account(1, 'Demo', 'demo@gmail.com', '978675')

        # Check if the account is created successfully
        self.assertIsNotNone(acc)
        self.assertEqual(acc.account_id, 1)
        self.assertEqual(acc.balance, 0.0)
        self.assertEqual(acc.get_balance(), 0.0)
        

if __name__ == '__main__':
    unittest.main()
