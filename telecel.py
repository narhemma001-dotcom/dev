import re
import random
import datetime
class Telecel:
    def __init__(self,momo_pin= None,account_num=None,balance = 0,with_amount=None, trans_amount=None,time = None,time1 =None,):
        self.momo_pin = momo_pin
        self.balance = balance
        self.account_num = account_num
        self.time1 = time
        self.time2 = time1
        self.trans_amount = trans_amount 
        self.with_amount = with_amount
    def __str__(self):
        return f"{self.balance} {self.time1}{self.time2}{self.trans_amount}{self.with_amount} {self.momo_pin}"

    def user(self):
        user_info={
            "momo_pin": None,
            "account_num":None
        }
        while True:
            pin =input("Create a 4-digit pin: ")
            if re.fullmatch(r"^\d{4}$",pin):       
                user_info["momo_pin"]= pin
                self.momo_pin = pin    
            else:
                print("Invalid pin.\nEnsure it is a 4-digit pin\nTry again")
                exit()
            break              
        user_info["account_num"]= random.randrange(10000000,99999999)
        self.account_num = user_info["account_num"]   
    
    
    def check_pin(self,mode = None):
        pin =input("Enter the 4-digit pin: ")
        if re.fullmatch(r"^\d{4}$",pin) and pin == self.momo_pin:
            return True
        else:
            print("Invalid pin..")
            return False
        
    def check_telestarNum(self,mode = None):
        while True:
            phone_num = input("Enter recipient's phone number: ")
            if re.fullmatch(r"^(059)\d{7}$",phone_num):
                pass
                break
            else:
                print("Invalid number..")    

    def check_otherNum(self,mode= None):
        while True:
            phone_num = input("Enter recipient's phone number: ")
            if re.fullmatch(r"^(050|026|023)\d{7}$",phone_num):
                pass
                break
            else:
                print("Invalid number..")

    def transfer_money(self,mode = None):
        try:    
            amount_transfer =int(input("Enter amount to transfer: "))
            self.trans_amount = amount_transfer
            if amount_transfer > self.balance:
                print("Insufficient balance..")
            else:
                self.check_pin()
                charge = 0.1 * amount_transfer 
                self.balance -= (amount_transfer + charge)   
                print(f"Your current balance is {self.balance:.2f}\nCharge is {charge}")
            timestap = datetime.datetime.now()
            self.time1 = timestap
        except ValueError:
           print("Invalid input.") 
        except NameError:
            print("Invalid input!")
    def cash_out(self,mode = None):
        try:
            withdraw_amount = int(input("Enter withdraw amount: "))
            self.with_amount = withdraw_amount
            if withdraw_amount > self.balance:
                print("Insufficient balance..")
            else:
                self.check_pin()
                charge = 0.05 * withdraw_amount
                self.balance -= (withdraw_amount + charge)
                print(f"Withdraw successful..\nCharge is {charge}\nCurrent balance is {self.balance:.2f}")    
            timestap2 = datetime.datetime.now()
            self.time2 = timestap2
            return self.with_amount,self.balance,self.time2
        except ValueError:
           print("Invalid input.") 
        except NameError:
            print("Invalid input!")        
    def momo_pay(self):
        try:
            merchantID = input("Enter the 6-digit Merchant ID: ")
            if re.fullmatch(r"^\d{6}$",merchantID):
                amount = int(input("Enter the amount to pay: "))  
                if amount > self.balance:
                    print("Insufficient balance..")
                elif amount > 100:
                    charge = 0.01 * amount
                    self.balance -= (amount + charge)
                    print(f"Payment successful..\nYour current balance is {self.balance:.2f}\nCharge is {charge}")
                else:
                  self.balance -= amount
                  charge = 0
                  print(f"Payment successful..\nYour current balance is {self.balance:.2f}\nCharge is {charge}")
        except ValueError:
           print("Invalid input.") 
        except NameError:
            print("Invalid input!")       
    
    def airtime_bundle(self,mode = None):
        try:
            airtime_bundle = int(input("1.Buy Airtime\n2.Buy Bundles\n"))
            if airtime_bundle == 1:
                airtime_amount = int(input("Enter airtime amount: "))
                if airtime_amount > self.balance:
                    print("insuficient balance, try again")
                else:
                    print("Airtime successfully purchased..")
                    self.balance-=airtime_amount
                    print(f"Your current balance is {self.balance}")
            else:
                bundle_amount = int(input("1.GHC 5 (280 MB)\n2.GHC 10 (667 MB)\n3.GHC 100(10 GB)\n4.Flexi-Bundle(GHS 0 - GHS 400)"))
                if bundle_amount == 1:
                    if 5 > self.balance :
                        print("Insufficient balance.")
                    else:    
                        self.balance -= 5
                        print(f"Successfully purchased..\nYour current balance is {self.balance}")      
                elif bundle_amount == 2:
                    if 10 > self.balance:
                        print("Insufficient balance")
                    else:    
                        self.balance-= 10
                        print(f"Successfully purchased..\nYour current balance is {self.balance}")           
                elif bundle_amount == 3:
                    if 100 > self.balance:
                        print("Insufficient balance")
                    else:    
                        self.balance-=100
                        print(f"Successfully purchased..\nYour current balance is {self.balance}")          
                else:
                    amount = int(input("Enter amount to purchase: "))
                    if amount > self.balance:
                        print("Insufficient balance")
                    else:    
                       self.balance-= amount
                       data = amount/(0.01786) * (0.05 * amount)
                       print(f"{data:.2f} MB Data Bundle successfully purchased.\nNew balance: {self.balance:.2f} ") 
        except ValueError:
           print("Invalid input.") 
        except NameError:
            print("Invalid input!")          
                  
    def my_Wallet(self, mode = None):
      while True:
        try:      
            wallet = int(input("1.Top Up Balance\n2.Check Balance\n3.Change MoMo Pin\n4.Transaction History\n"))
            if wallet == 1:
                deposit_amount = int(input("Enter amount to top up your balance: "))
                self.balance += deposit_amount   
                print(f"Balance top up is successful..\nYour new balance is {self.balance}")
            elif wallet == 2 :
                print(f"Your current balance is: {self.balance}")   
            elif wallet == 3:
                if self.check_pin():
                    new_pin = input("Enter your new 4-digit MoMO Pin: ")
                    self.momo_pin = new_pin
                    print("MOMO Pin successfully changed!") 
            elif wallet == 4 :
                    print(
                    "Transaction History:\n" \
                    "_____________________________________________\n" \
                    f"Timestamp   : {self.time1}\n"
                    f"Type        :  Transfer    \n"
                    f"Amount (GHS):  {self.trans_amount}          \n"    
                    
                    "Transaction History:\n"
                    "_____________________________________________\n"
                    f"Timestamp   :  {self.time2}\n"
                    f"Type        :  Cash Out   \n"
                    f"Amount      :   {self.with_amount}"
                    )
            break
        except ValueError:
           print("Invalid input.") 
        except NameError:
            print("Invalid input!")       
            
telecel = None
try:
    hashcode = input("Enter the hashcode: ").strip() 
    telecel = Telecel()       
    if hashcode != "*150#":
        for i in range(3): 
            print(f"Ensure the hashcode is correct\nattempt {i+1}")
            hashcode = input("Enter the hashcode: ").strip()
            if hashcode == "*150#":
                break
        else:
            exit()  
except ValueError:
    print("Invalid input.") 
except NameError:
    print("Invalid input!")        

def main():  
    if hashcode == "*150#":
        telecel.user()
    while True:
        try:            
            num = int(input("Welcome to Telestar Mobile Money! Please select an option:\n1.Transfar Money\n2.MoMo Pay\n3.Airtime and Bundle\n4.Allow Cash Out\n5.My Wallet\n "))
            if num == 1:
                n = int(input("1.Telestar\n2.Other Networks\n"))
                if n == 1:
                    telecel.check_telestarNum()
                    telecel.transfer_money()
                elif n == 2:
                    telecel.check_otherNum()
                    telecel.transfer_money()
                else:
                    print("Invalid input, ensure input is 1 or 2")    
            elif num == 2:
                telecel.momo_pay()
            elif num == 3:
                telecel.airtime_bundle()
            elif num == 4:   
                telecel.cash_out()
            elif num == 5:
                telecel.my_Wallet()
            else:
                print("Invalid input, ensure your input is 1 - 5")                         
            x = input("Do you want to continue?(yes/no): ").lower() 
            if x == "no":
              break  
        except ValueError:
          print("Invalid input.") 

        except NameError:
            print("Invalid input!") 

if __name__ == "__main__":
    main()            
