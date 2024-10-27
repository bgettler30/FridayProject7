# Define a class for the bank account
class BankAccount:
    def __init__(self, account_number, balance=0):
        """Initialize the bank account with an account number and a starting balance."""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        """Display the current balance of the account."""
        print(f"Current balance: ${self.balance}")

# Create an instance (account) of BankAccount
my_account = BankAccount("5491647", 0)

# Indefinite loop to interact with the user's bank account
while True:
    print("\n--- Bank Account Menu ---")
    print("1: Deposit Money")
    print("2: Withdraw Money")
    print("3: Check Balance")
    print("4: Exit")

    # Prompt the user for input
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        my_account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw(amount)

    elif choice == "3":
        my_account.check_balance()

    elif choice == "4":
        print("Thank you for using our service. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
