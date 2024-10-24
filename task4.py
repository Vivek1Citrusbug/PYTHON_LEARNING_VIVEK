from datetime import datetime
import re

name_pattern = r"^[A-Za-z\s]+$"
account_pin_pattern = r"^[0-9]+$"
account_balance_pattern = r"^[0-9]+$"


def validate_name(name):
    if re.match(name_pattern, name):
        return True
    else:
        print("\nName should contain only alphabets.")
        return False


def validate_account_pin(account_pin):
    if re.match(account_pin_pattern, account_pin):
        return True
    else:
        print("\nAccount PIN should contain only digits.")
        return False


def validate_account_balance(account_balance):
    if account_balance.strip() == "":
        print("\nAmount can not be empty")
        return False
    elif re.match(account_balance_pattern, account_balance):
        return True
    else:
        print("\nEnter valid amount")
        return False


class Account:
    def __init__(self, name, account_pin, account_balance=0) -> None:
        self.name = name
        self.account_pin = account_pin
        self.account_balance = account_balance
        self.transaction_history: list[dict] = []

    def check_pin(self, account_pin):
        return self.account_pin == account_pin

    def withdraw(self, amount):
        if self.account_balance < int(amount):
            return False
        else:
            self.account_balance -= int(amount)
            self.record_transaction("withdraw", amount)
            return True

    def deposit(self, amount):
        self.account_balance += int(amount)
        self.record_transaction("Deposit", amount)

    def update_information(self, name, account_pin):
        if name:
            self.name = name
        if account_pin:
            self.account_pin = account_pin

    def record_transaction(self, transaction_type, amount):
        self.transaction_history.append(
            {
                "type": transaction_type,
                "amount": amount,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )


class ATM:

    def __init__(self) -> None:
        self.accounts: dict[int, Account] = {}

    def create_account(self):
        """Function creates account"""

        while True:
            name = input("\nEnter your name: ")
            if validate_name(name):
                break

        while True:
            account_pin = input("\nSet your account pin (digits only): ")
            if validate_account_pin(account_pin):
                break

        while True:
            account_balance = input("\nAdd your bank balance in integer: ")
            if validate_account_balance(account_balance):
                account_balance = int(account_balance)
                break

        account_number = len(self.accounts) + 1
        self.accounts[account_number] = Account(name, account_pin, account_balance)
        print(
            f"\nAccount created successfully! Your account number is {account_number}."
        )

    def login(self):
        """Function is used for Login into existing account"""

        account_number = int(input("\nEnter your account number : "))
        account_pin = input("\nEnter your account pin : ")

        account = self.accounts.get(account_number)
        if account and account.check_pin(account_pin):
            print("\nLogged in Successfully ... ")
            return account
        else:
            print("\nInvalid account number and pin")
            return None

    def balance_inquiry(self, account):
        """Function is used to fetch account balance"""

        print(f"\nYour current balance is: INR", account.account_balance)

    def cash_withdraw(self, account):
        """Function is used to withdraw money from account"""

        amount = input("\nEnter the amount you want to withdraw: ")
        if validate_account_balance(amount):
            if account.withdraw(amount):
                print(f"\nWithdrawal successful!")
            else:
                print("\nInsufficient fund")

    def deposit_money(self, account):
        """Function is used to deposit money in account"""

        amount = input("\nEnter the amount you want to deposit: ")
        if validate_account_balance(amount):
            account.deposit(amount)
            print(f"\nDeposit successful!")
        else:
            print("Please enter valid amount to deposit")

    def update_account_info(self, account):
        """Function is used to update user name and account pin"""

        while True:
            new_name = input("\nEnter Your New Name or leave blank to skip").strip()
            if new_name == "" or validate_name(new_name):
                break
        while True:
            new_pin = input("\nEnter Your New Pin")
            if validate_account_pin(new_pin):
                break

        account.update_information(
            new_name if new_name else None, new_pin if new_pin else None
        )
        print("\nAccount Information updated successfully")

    def transaction_history(self, account):
        """Function used for checking transaction history"""

        print("Transaction History:")
        for transaction in account.transaction_history:
            print(
                f"{transaction['date']}: {transaction['type']} - {transaction['amount']} INR"
            )


def main():
    atm = ATM()
    while True:
        print("\nATM Menu")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        selected_option = int(input("\nSelect your option : "))

        match selected_option:
            case 1:
                atm.create_account()
            case 2:
                account = atm.login()
                if account:
                    while True:
                        print("\n Account Menu")
                        print("\n 1. Balance Inquiry")
                        print("\n 2. Cash Withdrawal")
                        print("\n 3. Deposit")
                        print("\n 4. Update Account Information")
                        print("\n 5. Transaction History")
                        print("\n 6. Logout")

                        selected_choice = int(input("\nSelect option : "))
                        match selected_choice:
                            case 1:
                                atm.balance_inquiry(account)
                            case 2:
                                atm.cash_withdraw(account)
                            case 3:
                                atm.deposit_money(account)
                            case 4:
                                atm.update_account_info(account)
                            case 5:
                                atm.transaction_history(account)
                            case 6:
                                print("\nLogging out .... ")
                                break
                            case default:
                                print("\nInvalid option. please try again")

            case 3:
                print("\nExiting")
                break
            case default:
                print("\nEnter valid option")


if __name__ == "__main__":
    main()
