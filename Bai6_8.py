class Bank:
    Account_type = "Savings"
    location = "Guntur"
    
    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repr__(self):
        return f"Account: {self.name} - Acc Number: {self.Account_Number} - Balance: ${self.balance:.2f}"

    def start_atm(self):
        print("Welcome to the SSI ATM Machine")
        print("**************")
        self.authenticate()

    def authenticate(self):
        try:
            pin = int(input("Please enter your pin number: "))
            if pin == 123:  # Default PIN is 123
                self.account_menu()
            else:
                print("Pin Incorrect. Please try again")
                self.authenticate()
        except ValueError:
            print("Please enter a valid number!")
            self.authenticate()

    def account_menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1) Check Balance")
            print("2) Withdraw")
            print("3) Deposit")
            print("4) Quit")
            print("----------------")
            
            choice = input("Please select an option (1-4): ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                print("Thank you for using SSI ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def check_balance(self):
        print(f"Your Card Number: {self.Account_Number}")
        print(f"Your current balance: ${self.balance:.2f}")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrawal successful! ${amount:.2f} has been withdrawn.")
                    print(f"Remaining balance: ${self.balance:.2f}")
                else:
                    print("Insufficient funds!")
            else:
                print("Invalid amount! Please enter positive number.")
        except ValueError:
            print("Please enter a valid number!")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                self.balance += amount
                print(f"Deposit successful! ${amount:.2f} has been deposited.")
                print(f"New balance: ${self.balance:.2f}")
            else:
                print("Invalid amount! Please enter positive number.")
        except ValueError:
            print("Please enter a valid number!")

# Demo sử dụng chương trình ATM
if __name__ == "__main__":
    # Create bank account
    customer = Bank("John Doe", "XXXX XXXX XXXX 1337", 1000.00)
    
    # Start ATM machine
    customer.start_atm()