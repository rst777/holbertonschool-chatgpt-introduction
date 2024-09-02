class Checkbook:
    """
    The Checkbook class represents a simple check book allowing to manage an account balance
With deposit operations, withdrawal, and consultation of the balance.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("The amount of the deposit must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("The amount of withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
        print("Withdrew ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
