# Task 3: ATM Withdrawal System
# This program asks for PIN and account balance,
# then allows valid withdrawals using a function.

def withdraw(bal, amount):
    if amount <= 0:
        print("Invalid amount.")
        return bal

    if amount > bal:
        print("Insufficient balance.")
        return bal

    if amount % 500 != 0:
        print("Amount must be a multiple of 500.")
        return bal

    bal = bal - amount
    print("Withdrawal successful.")
    print("Remaining balance:", bal)
    return bal

c_pin = "1234"

e_pin = input("Enter your PIN: ")

if e_pin != c_pin:
    print("Wrong PIN. Access denied.")
else:
    acc_num = input("Enter your account number: ")
    bal = float(input("Enter your account balance: "))

    while True:
        amount = float(input("\nEnter withdrawal amount (0 to exit): "))

        if amount == 0:
            print("Transaction ended. Thank you.")
            break

        bal = withdraw(bal, amount)