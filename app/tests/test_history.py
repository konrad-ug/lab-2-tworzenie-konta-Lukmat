import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    company_name = "Januszex sp. z o.o"
    nip = "6289735952"

    def test_save_incoming_transfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.process_incoming_transfer(500)
        account.process_outgoing_transfer(300)
        account.process_outgoing_express_transfer(100)
        self.assertListEqual(account.history, [500, -300, -100, -1])

    def test_save_incoming_transfer_for_company_accounts(self):
        account = KontoFirmowe(self.company_name, self.nip)
        account.process_incoming_transfer(500)
        account.process_outgoing_transfer(300)
        account.process_outgoing_express_transfer(100)
        self.assertListEqual(account.history, [500, -300, -100, -5])