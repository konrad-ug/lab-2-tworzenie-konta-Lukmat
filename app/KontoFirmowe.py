from calendar import c
from app.Konto import Konto
import requests
import os
import datetime


class KontoFirmowe:
    charge_for_express_transfer = 5
    def __init__(self, company_name, nip):
        self.company_name = company_name
        if self.is_nip_correct(nip):
            self.nip = nip
        else:
            self.nip = "Pranie!"
        self.balance = 0
        self.history = []
    
    def is_nip_correct(self, nip):
        return len(nip) == 10 and self.is_nip_in_gov(nip)

    def is_nip_in_gov(self, nip):
        url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        nip_path = f"{url}api/search/nip/{nip}/?date={today}"
        response = requests.get(nip_path)
        print(f"Response dla nipu: {response.status_code}, {response.json()}")
        if response.status_code == 200:
            return True
        return False

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
        if self.is_balance_twice_as_big_as_loan(ammount) and self.is_transfer_to_zus():
            self.balance += ammount
            return True
        return False

    def is_balance_twice_as_big_as_loan(self, ammount: int):
        if self.balance > (ammount * 2):
            return True
        return False

    def is_transfer_to_zus(self):
        for i in self.history:
            if i == -1775:
                return True
        return False



    