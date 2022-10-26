import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    lastname = "Januszewski"
    pesel = "02310634908"
    saldo = 0
    coupon = "PROM_XYZ"

    peselElderly = "57111578656"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.name, self.lastname, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.name, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.lastname, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, self.saldo, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")

    #tutaj proszę dodawać nowe testy

    def test_pesel_is_wrong_length(self):
        wrongPesel = "123456789"
        account = Konto(self.name, self.lastname, wrongPesel)
        self.assertEqual(account.pesel, "Niepoprawny pesel!", "Pesel nie jest równy 'Niepoprawny pesel!', gdy ma złą długość!")

    def test_saldo_is_50_when_coupon_is_valid(self):
        account = Konto(self.name, self.lastname, self.pesel, self.coupon)
        self.assertEqual(account.saldo, 50, "Saldo nie jest równe 50 po użyciu kuponu!")

    def test_saldo_is_0_when_coupon_is_invalid(self):
        account = Konto(self.name, self.lastname, self.pesel, "PROMO_XYZ")
        self.assertEqual(account.saldo, 0, "Saldo nie jest równe 0 po użyciu niepoprawnego kuponu!")

        account = Konto(self.name, self.lastname, self.pesel)
        self.assertEqual(account.saldo, 0, "Saldo nie jest równe 0 po nie wprowadzeniu kuponu!")

    def test_coupon_is_invalid_for_elderly(self):
        account = Konto(self.name, self.lastname, self.peselElderly, self.coupon)
        self.assertEqual(account.saldo, 0, "Kupon jest ważny dla osób urodzonych przed 1960 roku!")

    