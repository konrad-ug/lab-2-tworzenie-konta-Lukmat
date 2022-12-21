import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    company_name = "Januszex sp. z o.o"
    nip = "5252674798"

    def test_save_incoming_transfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.process_incoming_transfer(500)
        account.process_outgoing_transfer(300)
        account.process_outgoing_express_transfer(100)
        self.assertListEqual(account.history, [500, -300, -100, -1])

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_in_gov')
    def test_save_incoming_transfer_for_company_accounts(self, mock_is_nip_in_gov):
        mock_is_nip_in_gov.return_value = True
        account = KontoFirmowe(self.company_name, self.nip)
        account.process_incoming_transfer(500)
        account.process_outgoing_transfer(300)
        account.process_outgoing_express_transfer(100)
        self.assertListEqual(account.history, [500, -300, -100, -5])