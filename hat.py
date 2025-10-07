import random

class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
           return self.account_holder
    @classmethod
    def user(cls):
        _user ={
            "account_number" : None,
            "account_holder" : None,
            "balance": 0  
        }
        _user["account_holder"]=  input("Enter your name: ").strip().title()
        _user["account_number"]= random.randrange(10000000,99999999)
        
        return cls(**_user)
    
    def deposit(self):
        deposit = int(input("Enter deposite amount: "))
        self.balance+= deposit
        return self.balance
    
    def withdraw(self):
        withdraw = int(input("Enter withdraw amount: "))
        self.balance -= withdraw
        return self.balance
    
    def get_balance(self):
        return f"Your current balance is {self.balance:.2f}"
bank = None
print("Welcome..")
while True:
    select= int(input("Select one:\n1.Create an account\n2.Deposite money\n3.Withdraw money\n4.Check balance\n"))        
    if select == 1:
        bank =BankAccount.user()
        print("Account successfully created..")
    else:
        print("You need to create an account first..")   
    if select == 2:
        bank.deposit()
    elif select == 3:
        bank.withdraw()
    elif select == 4:
        bank.get_balance()         
    x = input("Do youwant to continue (yes/no):").strip().lower()
    if x == "no":
        break
