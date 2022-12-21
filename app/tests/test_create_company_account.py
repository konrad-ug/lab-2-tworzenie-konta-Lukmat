import unittest

from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch

class TestCreateCompanyBankAccount(unittest.TestCase):
    company_name = "Januszex sp. z o.o"
    nip = "5252674798"

    @patch('app.KontoFirmowe.KontoFirmowe.is_nip_in_gov')
    def test_creating_account(self, mock_is_nip_in_gov):
        mock_is_nip_in_gov.return_value = True
        first_account = KontoFirmowe(self.company_name, self.nip)

        self.assertEqual(first_account.company_name, self.company_name, "Nazwa firmy nie została zapisana")
        self.assertEqual(first_account.balance, 0, "Saldo nie jest zerowe!")
        self.assertEqual(first_account.nip, self.nip, "NIP nie jest poprawny!")

    def test_nip_too_long(self):
        account = KontoFirmowe(self.company_name, "6289735952342")
        self.assertEqual(account.nip, "Pranie!", "NIP jest za długi")

    def test_nip_too_short(self):
        account = KontoFirmowe(self.company_name, "62897")
        self.assertEqual(account.nip, "Pranie!", "NIP jest za krótki")

    

