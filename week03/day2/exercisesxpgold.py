#part1
# Base version of BankAccount (will be replaced by updated one below)
# Kept here for exercise clarity

#part2
class MinimumBalanceAccount:
    def __init__(self, username, password, balance=0, minimum_balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False
        self.minimum_balance = minimum_balance

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Invalid login credentials")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in to deposit")
        if amount <= 0:
            raise Exception("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in to withdraw")
        if amount <= 0:
            raise Exception("Withdrawal must be positive")
        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: balance would go below minimum")
        self.balance -= amount

#part3
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Invalid login credentials")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in to deposit")
        if amount <= 0:
            raise Exception("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be logged in to withdraw")
        if amount <= 0:
            raise Exception("Withdrawal must be positive")
        self.balance -= amount

#part4
class ATM:
    def __init__(self, account_list, try_limit):
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("All accounts must be BankAccount or MinimumBalanceAccount")

        if try_limit <= 0:
            print("Invalid try limit. Defaulting to 2.")
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            choice = input("\n1. Log in\n2. Exit\nChoose an option: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            try:
                account.authenticate(username, password)
                print(f"Welcome, {username}!")
                self.show_account_menu(account)
                return
            except:
                continue

        self.current_tries += 1
        print("Incorrect credentials.")

        if self.current_tries >= self.try_limit:
            print("Too many failed attempts. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print(f"\nCurrent balance: {account.balance}")
            action = input("1. Deposit\n2. Withdraw\n3. Exit\nChoose an action: ")
            if action == '1':
                try:
                    amount = int(input("Amount to deposit: "))
                    account.deposit(amount)
                except Exception as e:
                    print(e)
            elif action == '2':
                try:
                    amount = int(input("Amount to withdraw: "))
                    account.withdraw(amount)
                except Exception as e:
                    print(e)
            elif action == '3':
                print("Logging out.")
                break
            else:
                print("Invalid choice.")

# launcher code
if __name__ == "__main__":
    acc1 = BankAccount("john", "1234", 500)
    acc2 = MinimumBalanceAccount("jane", "5678", 1000, minimum_balance=200)

    atm = ATM([acc1, acc2], 3)
