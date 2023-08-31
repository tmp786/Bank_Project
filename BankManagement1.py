#BANKING MANAGEMENT

class Bank_Account():
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance

    def check_password(self, password):
        return self.password == password


    def Deposit(self, amount):
        self.balance += amount
        print(f"\n Deposit Amount : {amount}\n Total Balance :  {self.balance}")


    def Withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\n Withdraw Amount :  {amount}\n Reamning Balance : {self.balance}")


    def get_balance(self):
        return  self.balance

    def Mini_statement(self):
        print("Mini statement: ")
        print(f"Username : {self.username}")
        print(f"Current balance : {self.balance}")

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password):
        if username in self.accounts:
            print("Username already Exits")
        else:
            self.accounts[username] = Bank_Account(username, password)
            print(" \n Bank_Account created successfully" )
            print("----------- Welcome To X National Bank ----------------")

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts [username]
            if account.password == password:
                print("Login Success.... ")
                return account
            else:
                print("Invalid Password")
        else:
            print("Invalid username")
        return None

if __name__ == '__main__':
    bank = BankingSystem()

    while True:
        print("\n")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        option = int(input("Enter Your Option (1-3) : "))

        if option == 1:
            username = input("Enter Username : ")
            password = input("Enter Pin : ")
            bank.create_account(username, password)

        elif option == 2:
            username = input("Enter Username : ")
            password = input("Enter Pin : ")
            account = bank.login(username, password)
            if account is not None:
                while True:
                    print("\n-------Welcome To X National Bank")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. MiniStatement")
                    print("5. EXit")
                    option = input("Enter Your Option(1-5) : ")

                    if option == '1':
                        amount = int(input("Enter Deposit Amount : "))
                        account.Deposit(amount)

                    elif option == '2':
                        amount = int(input("Enter Withdraw Amount : "))
                        account.Withdraw(amount)

                    elif option == '3':
                        print(f"Current Balance : {account.get_balance()}")

                    elif option == '4':
                        account.Mini_statement()

                    elif option == '5':
                        print("\n-------------Thank You Visit Again---------")
                        break
                    else:
                        print("Invalid Option")

        elif option == 3:
            print("\n ----------Thank You-----------")
            break

        else:
            print("Invalid Choice")
