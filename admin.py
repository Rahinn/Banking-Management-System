from user import Bank

class Admin:
    @staticmethod
    def check_total_loan_amount():
        print(f"Total loan amount: {Bank.total_loan_amount}")

    @staticmethod
    def check_total_bank_balance():
        print(f"Total bank balance: {Bank.bank_balance}")

    @staticmethod
    def enable_loan_feature():
        Bank.loan_enabled = True
        print("Loan feature has been enabled.")

    @staticmethod
    def disable_loan_feature():
        Bank.loan_enabled = False
        print("Loan feature has been disabled.")
