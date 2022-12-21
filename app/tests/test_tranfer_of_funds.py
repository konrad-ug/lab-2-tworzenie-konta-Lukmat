import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

class TestProcessTransfers(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"

    company_name = "Januszex sp. z o.o"
    nip = "5252674798"

    def test_successful_outgoing_tranfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 1000
        account.process_outgoing_transfer(800)
        self.assertEqual(account.balance, 1000 - 800)

    def test_unsuccessful_outgoing_transfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 1000
        account.process_outgoing_transfer(1200)
        self.assertEqual(account.balance, 1000)

    def test_successful_incoming_tranfer(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 0
        account.process_incoming_transfer(800)
        self.assertEqual(account.balance, 0 + 800)

    def test_series_of_transfers(self):
        account = Konto(self.name, self.lastname, self.pesel)
        account.balance = 0
        account.process_incoming_transfer(2000)
        account.process_outgoing_transfer(1000)
        account.process_outgoing_transfer(1500)
        account.process_incoming_transfer(200)
        self.assertEqual(account.balance, 1200)

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_in_gov')
    def test_successful_outgoing_tranfer_for_company_accounts(self, mock_is_nip_in_gov):
        mock_is_nip_in_gov.return_value = True
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 1000
        account.process_outgoing_transfer(800)
        self.assertEqual(account.balance, 1000 - 800)

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_in_gov')
    def test_unsuccessful_outgoing_transfer_for_company_accounts(self, mock_is_nip_in_gov):
        mock_is_nip_in_gov.return_value = True
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 1000
        account.process_outgoing_transfer(1200)
        self.assertEqual(account.balance, 1000)

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_in_gov')
    def test_successful_incoming_tranfer_for_company_accounts(self, mock_is_nip_in_gov):
        mock_is_nip_in_gov.return_value = True
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 0
        account.process_incoming_transfer(800)
        self.assertEqual(account.balance, 0 + 800)

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_in_gov')
    def test_series_of_transfers_for_company_accounts(self, mock_is_nip_in_gov):
        mock_is_nip_in_gov.return_value = True
        account = KontoFirmowe(self.company_name, self.nip)
        account.balance = 0
        account.process_incoming_transfer(2000)
        account.process_outgoing_transfer(1000)
        account.process_outgoing_transfer(1500)
        account.process_incoming_transfer(200)
        self.assertEqual(account.balance, 1200)



    

