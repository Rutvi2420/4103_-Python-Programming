"""
6. Banking System Using Functions
Deposit
Withdraw
Check Balance
"""

balance = 0

# Deposit Money
def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited:", amount)
    print("Updated Balance:", balance)

# Withdraw Money
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Amount Withdrawn:", amount)
        print("Updated Balance:", balance)

# Check Balance
def check_balance():
    print("Current Balance:", balance)

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Thank you for using Banking System!")
        break

    else:
        print("Invalid Choice!")
