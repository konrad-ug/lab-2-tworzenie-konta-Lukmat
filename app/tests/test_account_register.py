import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestAccountRegister(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    @classmethod
    def setUpClass(self):
        self.account = Konto(self.name, self.lastname, self.pesel)

    def test_1_add_account(self):
        RejestrKont.add_account(self.account)
        self.assertIn(self.account, RejestrKont.accounts)

    def test_2_find_account(self):
        RejestrKont.add_account(self.account)
        self.assertEqual(self.account, RejestrKont.find_account(self.account.pesel))

    def test_3_count_accounts(self):
        RejestrKont.add_account(self.account)
        self.assertEqual(3, RejestrKont.count_accounts())
    
    @classmethod
    def tearDownClass(cls):
        cls.accounts = []

