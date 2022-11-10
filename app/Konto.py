from calendar import c
import re


class Konto:
    charge_for_express_transfer = 1
    def __init__(self, name, lastname, pesel, coupon=""):
        self.name = name
        self.lastname = lastname
        self.history = []
        
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
            self.balance = 50
        else:
            self.balance = 0

    def process_outgoing_transfer(self, ammount: int):
        if self.balance - ammount < 0:
            self.balance = self.balance
        else:
            self.balance -= ammount
            self.history.append(-ammount)

    def process_incoming_transfer(self, ammount: int):
        self.balance += ammount
        self.history.append(ammount)

    def process_outgoing_express_transfer(self, ammount: int):
        if self.balance - ammount < 0:
            self.balance = self.balance
        else:
            self.balance -= ammount
            self.balance -= self.charge_for_express_transfer
            self.history.append(-ammount)
            self.history.append(-self.charge_for_express_transfer)

    def take_out_loan(self, ammount: int):
        if len(self.history) < 3:
            return False
        if self.history[-1] > 0 and self.history[-2] > 0 and self.history[-3] > 0:
            self.balance += ammount
            return True
        if len(self.history) < 5:
            return False
        if sum(self.history[-5:]) > ammount:
            self.balance += ammount
            return True
        else:
            return False

