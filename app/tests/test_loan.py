import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    def setUp(self):
        self.account = Konto(self.name, self.lastname, self.pesel)

    def test_successful_loan_1(self):
        self.account.history = [-100, 100, 100, 100]
        is_granted = self.account.take_out_loan(500)
        self.assertTrue(is_granted)
        self.assertEqual(self.account.balance, 500)

    def test_successful_loan_2(self):
        self.account.history = [400, -50, 200, 100, -100]
        is_granted = self.account.take_out_loan(500)
        self.assertTrue(is_granted)
        self.assertEqual(self.account.balance, 500)

    def test_unsuccessful_loan_1(self):
        self.account.history = [-100, -100, 200, -100, 200]
        is_granted = self.account.take_out_loan(500)
        self.assertFalse(is_granted)
        self.assertEqual(self.account.balance, 0)

    def test_unsuccessful_loan_2(self):
        self.account.history = [-100, -100, 400, -100, 400]
        is_granted = self.account.take_out_loan(500)
        self.assertFalse(is_granted)
        self.assertEqual(self.account.balance, 0)

    def test_unsuccessful_loan_3(self):
        self.account.history = [-100, -100, 400, -100, 100]
        is_granted = self.account.take_out_loan(500)
        self.assertFalse(is_granted)
        self.assertEqual(self.account.balance, 0)

    def test_unsuccessful_loan_4(self):
        self.account.history = [100, 500]
        is_granted = self.account.take_out_loan(500)
        self.assertFalse(is_granted)
        self.assertEqual(self.account.balance, 0)

    def test_unsuccessful_loan_5(self):
        self.account.history = []
        is_granted = self.account.take_out_loan(500)
        self.assertFalse(is_granted)
        self.assertEqual(self.account.balance, 0)
    
    def test_unsuccessful_loan_6(self):
        self.account.history = [100, 200, 100, -200]
        is_granted = self.account.take_out_loan(500)
        self.assertFalse(is_granted)
        self.assertEqual(self.account.balance, 0)
    

