import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestAccountRegister(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    @classmethod
    def setUpClass(cls):
        account = Konto(cls.name, cls.lastname, cls.pesel)
        RejestrKont.add_account(account)

    def test_1_add_account(self):
        account = Konto(self.name, self.lastname, self.pesel)
        RejestrKont.add_account(account)
        self.assertIn(account, RejestrKont.accounts)

    def test_2_find_account(self):
        account = Konto(self.name, self.lastname, self.pesel)
        RejestrKont.add_account(account)
        self.assertEqual(account.pesel, RejestrKont.find_account(self.pesel).pesel)

    def test_3_count_accounts(self):
        account = Konto(self.name, self.lastname, self.pesel)
        RejestrKont.add_account(account)
        self.assertEqual(4, RejestrKont.count_accounts())
    
    @classmethod
    def tearDownClass(cls):
        cls.accounts = []

