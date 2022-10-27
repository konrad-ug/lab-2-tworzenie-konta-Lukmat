from calendar import c
import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, coupon=""):
        self.imie = imie
        self.nazwisko = nazwisko
        
        self.checkPesel(pesel)
        self.checkPromo(coupon)

    def checkPesel(self, pesel):
        if(len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def checkPromo(self, coupon):
        isValid = re.search("^PROM_", coupon) != None and len(coupon) == 8 and (int(self.pesel[0:2]) > 60 or int(self.pesel[2:4]) > 20)
        
        if(isValid):
            self.saldo = 50
        else:
            self.saldo = 0