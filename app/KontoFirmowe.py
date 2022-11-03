from calendar import c
from app.Konto import Konto


class KontoFirmowe:
    charge_for_express_transfer = 5
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if self.is_nip_correct(nip) else "Niepoprawny NIP!"
        self.balance = 0
        self.history = []
    
    def is_nip_correct(self, nip):
        return len(nip) == 10

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



    