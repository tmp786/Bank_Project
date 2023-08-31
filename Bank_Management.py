#BANKING MANAGEMENT
import random
import datetime
class Bank_Account():
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def check_password(self, password):
        return self.password == password
class Atm(Bank_Account):
    def bank_details(self,Deposit,Withdrawal,Ministatement,Exit):
        self.d = Deposit
        self.w = Withdrawal
        self.ms = Ministatement
        self.e = Exit

bank_accounts = [
    Bank_Account ("vigi","123")
]

login_bank_account = None

while True:
    print("1.Creata a SignUp Details  \n")
    print("2.SignIn ")
    choice = int(input("Enter The Choice : \n"))
    if choice == 1:
        username = input("Enter UserName : ")
        password = input("Enter Pin : ")
        bank_accounts.append(Bank_Account(username,password))
        print("Signup Successfully")
    elif choice == 2:
        username = input("Enter UserName : ")
        password = input("Enter Pin : ")
        for account in bank_accounts:
            if account.username == username and account.check_password(password):
                login_bank_account = account
                print(f"SignIn Successfully, {username}")
                break
        if login_bank_account is None:
            print("Invalid Inputs")

        else:
            print("Welcome to X National Bank")
            break

    else:
        print("Wrong Details")
    break

balances = 50000
deposits = []
withdrawal = []
debit = []
credit = []
while True:
    option = int(input(" 1.Choose Your option : "))
    if option == 1 :
        print("Your Balance  : ", balances, "Rs/-")
        break
    elif option == 2 :
        print("Your Previous Balance :", balances,"Rs/-")
        deposit = float(input("Enter Your Deposit Amount: "))
        print("Diposit Amount is successfuly")
        balances += deposit
        print("total amount",balances,"Rs/-")
        break
    elif option ==3 :
        withdrawal = float(input("Draw Your Amount: "))
        if withdrawal <= balances:
            balances -= withdrawal
            print("Your Balance Amount",balances,"Rs/-")
            # break
        else:
            print("Insufficent Balances")

    elif option == 4 :
        mini_statement = input("Check You Statement")
        bank_account = int(input("Enter Account number : "))
        debit = float(input("Enter Debit amount : "))
        current_time = datetime.datetime.now()
        if debit <= balances:
            balances -= debit
            print("your Debit Amount", balances, "Rs/-", current_time)
            print("Balance Amount", balances, "Rs/-")
            if debit <= balances:
                balances -= debit
                print("your Debit Amount", balances, "Rs/-", current_time)
                print("Balance Amount", balances, "Rs/-")
                if debit <= balances:
                    balances -= debit
                    print("your Debit Amount", balances, "Rs/-", current_time)
                    print("Balance Amount", balances,"Rs/-")
            credit = float(input("enter credit amount : "))
            balances += credit
            print("Credit Amount", balances, "Rs/-", current_time)
            print("Balance Amount", balances, "Rs/-")
            credit = float(input("enter credit amount : "))
            balances += credit
            print("Credit Amount",balances, "Rs/-", current_time)
            print("Balance Amount", balances, "Rs/-")
        else:
            print("Print Is Not Avilable")
    elif option == 5 :
        print("Exit")
        print("thank you using Atm \n")
        break
    else:
        print("Invalid Option")

        print("Try again")
    break




