import unittest
from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    company_name = "Januszex sp. z o.o"
    nip = "6289735952"

    def setUp(self):
        self.account = KontoFirmowe(self.company_name, self.nip)

    @parameterized.expand([
        ([100, 400, 250, -1775, -350], 5000, 2000, True, 7000),
        ([100, 400, 250, -1775, -350], 5000, 2500, False, 5000),
        ([100, 400, 250, -1775, -350], 5000, 3000, False, 5000),
        ([100, 400, 250, -1500, -350], 5000, 2000, False, 5000),
        ([100, 400, 250, -1500, -350], 5000, 2500, False, 5000),
        ([100, 400, 250, -1500, -350], 5000, 3000, False, 5000),
    ])

    def test_loan_company_account(self, history, balance, ammount, expected_loan_decision, expected_balance):
        self.account.history = history
        self.account.balance = balance
        is_granted = self.account.take_out_loan(ammount)
        self.assertEqual(is_granted, expected_loan_decision)
        self.assertEqual(self.account.balance, expected_balance)
