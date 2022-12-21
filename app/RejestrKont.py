from app.Konto import Konto

class RejestrKont():
    accounts = []

    @classmethod
    def add_account(cls, account):
        cls.accounts.append(account)

    @classmethod
    def find_account(cls, pesel):
        for account in cls.accounts:
            if account.pesel == pesel:
                return account

    @classmethod
    def count_accounts(cls):
        return len(cls.accounts)