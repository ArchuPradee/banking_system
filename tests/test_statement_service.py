# tests/test_statement_service.py
import unittest
from infra.account_repository import AccountRepository
from service.transaction_service import TransactionService
from service.account_service import AccountService
from service.statement_service import StatementService

class TestStatementService(unittest.TestCase):
    def setUp(self):
        acc_repo = AccountRepository()
        self.account_service = AccountService(acc_repo)
        self.transaction_service = TransactionService(acc_repo)
        self.statement_service = StatementService(acc_repo)

    def test_generate_account_statement(self):
        acc = self.account_service.create_account(1, 'Demo', 'demo@gmail.com', '978675')
        print(self.transaction_service.make_transaction(acc.account_id, 100, 'deposit'))
        print(self.transaction_service.make_transaction(acc.account_id, 50, 'withdraw'))
        stmt = self.statement_service.generate_account_statement(acc.account_id)
        stmt = stmt.split("\n")
        self.assertEqual(stmt[6], 'Transaction ID: 1, Amount: 100.0, Transaction_Type: deposit')
        self.assertEqual(stmt[7], 'Transaction ID: 2, Amount: 50.0, Transaction_Type: withdraw')

if __name__ == '__main__':
    unittest.main()
