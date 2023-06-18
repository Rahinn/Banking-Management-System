


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
        self.transaction_history = []
        self.loan_counter = 0
        self.bank_balance = 10000
        

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

    def get_transaction_history(self):
        return self.transaction_history


class Bank(User):
    Users = []
    bank_balance = 10000
    total_loan_amount = 0
    total_bank_balance = 0
    loan_enabled = True

    def create_account(self):
        Bank.Users.append(self)
        print("The account has been created successfully, and the account information is given below:")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

    def deposit_money(self, amount):
        self.balance += amount
        Bank.total_bank_balance+=amount
        transaction = f"Deposited {amount} into account"
        self.add_transaction(transaction)
        print(f"{amount} has been deposited into {self.name}'s account.")

    def withdraw_money(self, amount):
        if amount > self.balance:
            print("The amount is insufficient. Please try a lesser amount.")
        else:
            self.balance -= amount
            Bank.total_bank_balance-=amount
            transaction = f"Withdrew {amount} from account"
            self.add_transaction(transaction)
            print(f"{amount} has been withdrawn from {self.name}'s account.")

    def available_balance(self):
        return self.balance

    @classmethod
    def account_holders(cls):
        return len(cls.Users)

    def transfer_money(self,sender, recipient, amount):
        if amount > sender.balance:
            print(f'{sender.name} account has not enough money. please try later')
        elif recipient not in Bank.Users:
            print(f"{recipient.name}'s account not found.")
        else:
            sender.balance -= amount
            self.bank_balance-=amount
            recipient.balance += amount
            transaction1 = f"Transferred {amount} from {sender.name} to {recipient.name}'s account"
            transaction2 = f"Deposited {amount} from {sender.name} to {recipient.name}'s account"
            sender.add_transaction(transaction1)
            recipient.add_transaction(transaction2)
            print(f"{amount} has been transferred from {sender.name}'s account to {recipient.name}'s account.")

    def view_transaction_history(self):
        print(f"Transaction History for {self.name}:")
        for transaction in self.get_transaction_history():
            print(transaction)

    def take_loan(self):
        if self.loan_counter >= 2:
            print(f"{self.name} has already taken the maximum number of loans.")
        elif not Bank.loan_enabled:
            print("Loan feature is currently disabled.")
        else:
            loan_amount = self.balance * 2
            if loan_amount > Bank.bank_balance:
                print("The bank does not have enough money to give you a loan.")
            else:
                self.balance += loan_amount
                transaction = f"Loan taken: {loan_amount}"
                self.add_transaction(transaction)
                self.loan_counter += 1
                Bank.bank_balance -= loan_amount
                Bank.total_loan_amount+=loan_amount
                Bank.total_bank_balance-=loan_amount
                print(f"{self.name} has taken a loan of {loan_amount}.")
                print(f"New balance: {self.balance}")
