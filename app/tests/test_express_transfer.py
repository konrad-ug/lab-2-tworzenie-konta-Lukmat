from os import access
import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestExpressTransferFunds(unittest.TestCase):
    name = "Darek"
    lastname = "Januszewski"
    pesel = "72537583652"

    company_name = "Januszex sp. z o.o"
    nip = "6289735952"

    def test_successful_outgoing_express_transfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 1000
        account.process_outgoing_express_transfer(800)
        self.assertEqual(account.balance, 1000 - 800 - 1)

    def test_unsuccessful_outgoing_express_transfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 1000
        account.process_outgoing_express_transfer(1200)
        self.assertEqual(account.balance, 1000)

    def test_successful_outgoing_express_transfer_for_company_accounts(self):
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 1000
        account.process_outgoing_express_transfer(800)
        self.assertEqual(account.balance, 1000 - 800 - 5)

    def test_unsuccessful_outgoing_express_transfer_for_company_accounts(self):
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 1000
        account.process_outgoing_express_transfer(1200)
        self.assertEqual(account.balance, 1000)

    def test_successful_outgoing_express_transfer_balance_below_0(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 1000
        account.process_outgoing_express_transfer(1000)
        self.assertEqual(account.balance, 1000 - 1000 - 1)

    def test_successful_outgoing_express_transfer_for_company_accounts_balance_below_0(self):
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 1000
        account.process_outgoing_express_transfer(1000)
        self.assertEqual(account.balance, 1000 - 1000 - 5)