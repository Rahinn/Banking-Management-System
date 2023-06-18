





from user import Bank
from admin import Admin

def main():
    # Create instances of Bank and Admin
    Rahin = Bank("Rahin", "rahinahmed157@gmail.com")
    admin = Admin()

    # Create bank account
    Rahin.create_account()

    # Deposit money
    Rahin.deposit_money(500)

    # Withdraw money
    Rahin.withdraw_money(200)

    # Check available balance
    print(f"Available balance in {Rahin.name}'s account: {Rahin.available_balance()}")

    # Create another bank account
    Ruhan = Bank("Ruhan", "ruhanahmed134@gmail.com")
    Ruhan.create_account()

    # Transfer money
    Rahin.transfer_money(Rahin, Ruhan, 300)
    print(f"Available balance in {Ruhan.name}'s account: {Ruhan.available_balance()}")

    # Deposit more money
    Rahin.deposit_money(1000)

    

    # Take loan
    Rahin.take_loan()
    Rahin.take_loan()
    #Rahin.take_loan()
    
    Ruhan.take_loan()
    

    # Number of accounts have here in the bank
    total_accounts = Bank.account_holders()
    print(f"Total number of accounts: {total_accounts}")

    # cheking total balance available here in the bank
    admin.check_total_bank_balance()

    # check the amount of money has been given as loan
    admin.check_total_loan_amount()

    # loan facility enable and disable
    admin.enable_loan_feature()
    admin.disable_loan_feature()
    
    # View transaction history
    Rahin.view_transaction_history()
    Ruhan.view_transaction_history()


if __name__ == "__main__":
    main()
