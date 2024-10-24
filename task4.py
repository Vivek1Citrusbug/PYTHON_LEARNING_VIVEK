from datetime import datetime
import re
from typing import Optional
from cryptography.fernet import Fernet
import random
import time
import json
import os

name_pattern: str = r"^[A-Za-z\s]+$"
account_pin_pattern: str = r"^[0-9]{6}$"
account_balance_pattern: str = r"^[0-9]+$"


key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data: str) -> str:
    '''Encrypt given data'''

    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt_data(encrypted_data: str) -> str:
    '''Decrypt given data'''

    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

def generate_unique_id():
    '''Generate unique ID'''

    random_part = random.randint(100, 999)  
    time_part = int(time.time()) % 1000      
    unique_id = f"{random_part}{time_part}" 
    return unique_id


def validate_name(name: str) -> bool:
    '''This function validates username'''

    if re.match(name_pattern, name):
        return True
    else:
        print("\nName should contain only alphabets.")
        return False

def validate_account_pin(account_pin: str) -> bool:
    '''This function validates account pin'''

    if re.match(account_pin_pattern, account_pin):
        return True
    else:
        print("\nAccount PIN should contain only digits of length 6")
        return False


def validate_account_balance(account_balance: str) -> bool:
    '''This function validate account balance'''

    if account_balance.strip() == "":
        print("\nAmount can not be empty")
        return False
    elif re.match(account_balance_pattern, account_balance):
        return True
    else:
        print("\nEnter valid amount")
        return False

def add_details_to_json(account_number,name,account_pin,account_balance):
    '''Add data to accounts json file'''

    source_file_path = 'src/accounts.json'
    if os.path.exists(source_file_path):
        with open(source_file_path,'r') as accounts_json:
            try:
                json_data = json.load(accounts_json)
            except json.JSONDecodeError:
                json_data = []
    else:
            json_data = []
    
    new_account_data = {
        'account_number' : account_number,
        'username' : name,
        'account_pin' : account_pin,
        'account_balance' : account_balance,
        'account_transaction' : []
    }

    json_data.append(new_account_data)
    with open(source_file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
    print(f"New account data has been added to {source_file_path}")

def fetch_account_details(account_number):
    '''Function fetch account details from json file'''

    source_file_path = 'src/accounts.json'
    if os.path.exists(source_file_path):
        with open(source_file_path,'r') as accounts_json:
            try:
                json_data = json.load(accounts_json)
                if isinstance(json_data,list):
                    for account in json_data:
                        if account['account_number'] == account_number:
                            return account
                else:
                    return None      
            except json.JSONDecodeError:
                return None
    else:
        print("Source json not found")
        return None

class Account:
    def __init__(self, name: str,account_number:int ,account_pin: str, account_balance: str = "0") -> None:
        self.name: str = name
        self.account_number = account_number
        self.account_pin: str = account_pin
        self.account_balance: str = account_balance
        self.transaction_history: list[dict] = []

    def check_pin(self, account_pin: str) -> bool:
        '''Function checks user entered pin'''

        decrypted_pin = decrypt_data(self.account_pin)
        return account_pin == decrypted_pin

    def withdraw(self, amount: str) -> bool:
        '''Function performs withdraw operation'''

        decrypted_balance_str = decrypt_data(self.account_balance)
        if int(decrypted_balance_str) < int(amount):
            return False
        else:
            decrypted_balance = int(decrypted_balance_str) - int(amount)
            self.account_balance = encrypt_data(str(decrypted_balance))
            self.record_transaction("withdraw", amount)
            return True

    def deposit(self, amount: str) -> None:
        '''Function performs deposit operation'''

        decrypted_balance_str = decrypt_data(self.account_balance)
        decrypted_balance = int(decrypted_balance_str) + int(amount)
        self.account_balance = encrypt_data(str(decrypted_balance))
        self.record_transaction("Deposit", amount)

    def update_information(self, name: Optional[str], account_pin: Optional[str]) -> None:
        '''Function performs update information'''

        if name:
            self.name = name
        if account_pin:
            self.account_pin = account_pin

    def record_transaction(self, transaction_type: str, amount: str) -> None:
        '''Function records user transaction'''
        
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

    def create_account(self) -> None:
        """Function creates account"""

        while True:
            name: str = input("\nEnter your name: ")
            if validate_name(name):
                break

        while True:
            account_pin: str = input("\nSet your account pin (digits only): ")
            if validate_account_pin(account_pin):
                account_pin = encrypt_data(account_pin)
                break

        while True:
            account_balance: str = input("\nAdd your bank balance in integer: ")
            if validate_account_balance(account_balance):
                account_balance = encrypt_data(account_balance)
                break

        account_number: int = generate_unique_id()
        # self.accounts[account_number] = Account(name, account_number, account_pin, account_balance)
        add_details_to_json(str(account_number),name,account_pin,account_balance)
        print(f"\nAccount created successfully! Your account number is {account_number}.")

    def login(self) -> Optional[Account]:
        """Function is used for Login into existing account"""

        account_number: int = int(input("\nEnter your account number : "))
        account_pin: str = input("\nEnter your account pin : ")

        # account: Optional[Account] = self.accounts.get(account_number)
        account = fetch_account_details(str(account_number))
        print("\nReturned account details : ",account)
        if account:
            accountObj = Account(account['username'],account['account_number'], account['account_pin'], account['account_balance'])
            accountObj.transaction_history = account['account_transaction']
            if accountObj.check_pin(decrypt_data(account_pin)):
                print("\nLogged in Successfully ... ")
                return accountObj
            return None
        else:
            print("\nInvalid account number and pin")
            return None

    def balance_inquiry(self, account: Account) -> None:
        """Function is used to fetch account balance"""

        decrypted_balance = decrypt_data(account.account_balance)
        print(f"\nYour current balance is: INR", decrypted_balance)

    def cash_withdraw(self, account: Account) -> None:
        """Function is used to withdraw money from account"""

        amount: str = input("\nEnter the amount you want to withdraw: ")
        if validate_account_balance(amount):
            if account.withdraw(amount):
                print(f"\nWithdrawal successful!")
            else:
                print("\nInsufficient fund")

    def deposit_money(self, account: Account) -> None:
        """Function is used to deposit money in account"""

        amount: str = input("\nEnter the amount you want to deposit: ")
        if validate_account_balance(amount):
            account.deposit(amount)
            print(f"\nDeposit successful!")
        else:
            print("Please enter valid amount to deposit")

    def update_account_info(self, account: Account) -> None:
        """Function is used to update user name and account pin"""

        while True:
            new_name: str = input("\nEnter Your New Name or leave blank to skip: ").strip()
            if new_name == "" or validate_name(new_name):
                break
        while True:
            new_pin: str = input("\nEnter Your New Pin : ")
            if validate_account_pin(new_pin):
                new_pin = encrypt_data(new_pin)
                break

        account.update_information(
            new_name if new_name else None, new_pin if new_pin else None
        )
        print("\nAccount Information updated successfully")

    def transaction_history(self, account: Account) -> None:
        """Function used for checking transaction history"""

        print("Transaction History:")
        for transaction in account.transaction_history:
            print(
                f"{transaction['date']}: {transaction['type']} - {transaction['amount']} INR"
            )


def main() -> None:
    atm = ATM()
    while True:
        print("\nATM Menu")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        selected_option: int = int(input("\nSelect your option : ").strip() or 0)

        match selected_option:
            case 1:
                atm.create_account()
            case 2:
                account: Optional[Account] = atm.login()
                if account:
                    while True:
                        print("\nAccount Menu")
                        print("\n1. Balance Inquiry")
                        print("2. Cash Withdrawal")
                        print("3. Deposit")
                        print("4. Update Account Information")
                        print("5. Transaction History")
                        print("6. Logout")

                        selected_choice: int = int(input("\nSelect option : ").strip() or 0)
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
