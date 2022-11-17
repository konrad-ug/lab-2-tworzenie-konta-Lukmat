import unittest
from parameterized import parameterized

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    def setUp(self):
        self.account = Konto(self.name, self.lastname, self.pesel)

    @parameterized.expand([
        ([-100, 100, 100, 100], 500, True, 500),
        ([400, -50, 200, 100, -100], 500, True, 500),
        ([-100, -100, 200, -100, 200], 500, False, 0),
        ([-100, -100, 400, -100, 400], 500, False, 0),
        ([-100, -100, 400, -100, 100], 500, False, 0),
        ([100, 500], 500, False, 0),
        ([], 500, False, 0),
        ([100, 200, 100, -200], 500, False, 0),
    ])
    def test_loan(self, history, ammount, expected_loan_decision, expected_balance):
        self.account.history = history
        is_granted = self.account.take_out_loan(ammount)
        self.assertEqual(is_granted, expected_loan_decision)
        self.assertEqual(self.account.balance, expected_balance)
