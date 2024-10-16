class BankAccount:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.chances = 3

    def check_pin(self, user_pin):
        """Check if the entered PIN is correct."""
        if user_pin == self.pin:
            return True
        else:
            self.chances -= 1
            print(f"Wrong pin number. You have {self.chances} chances left.")
            return False

    def show_balance(self):
        """Display the current balance."""
        print(f"Your total balance is Rs.{self.balance}")

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        print(f"You have deposited Rs.{amount}. Your total balance is Rs.{self.balance}.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"You have withdrawn Rs.{amount}. Your total balance is Rs.{self.balance}.")

    def menu(self):
        """Show the menu options to the user."""
        while self.chances > 0:
            user_pin = int(input("Please enter the four-digit code: "))

            if self.check_pin(user_pin):
                while True:
                    user_choice = input("B: balance, D: deposit, W: withdraw. Please enter your choice: ").upper()

                    if user_choice == "B":
                        self.show_balance()

                    elif user_choice == "D":
                        deposit_amount = int(input("Enter the amount that you would like to deposit: "))
                        self.deposit(deposit_amount)

                    elif user_choice == "W":
                        withdraw_amount = int(input("Enter the amount you want to withdraw: "))
                        self.withdraw(withdraw_amount)

                    else:
                        print("Invalid choice, please select a valid option (B, D, or W).")

                    # Ask if user wants to exit
                    user_exit = input("Would you like to exit? Yes/No: ").lower()
                    if user_exit == "yes":
                        print("Thank you for using Arjun Bank!!")
                        return
                    elif user_exit == "no":
                        continue
                    else:
                        print("Invalid input. Exiting...")

            if self.chances == 0:
                print("You have used all your chances. Please try again later.")
                break


# Create an instance of BankAccount with pin 2809 and initial balance of Rs. 50000
account = BankAccount(pin=2809, balance=50000)

# Start the bank operations
print("Welcome to Arjun Bank !!")
account.menu()


