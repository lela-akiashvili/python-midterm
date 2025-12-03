import os

BALANCE_FILE = "balance.txt"  # Balance file
PINCODE_FILE = "pincode.txt"  # PIN code file


# Load or create PIN
def load_pin():
    if not os.path.exists(PINCODE_FILE):
        with open(PINCODE_FILE, "w") as file:
            file.write("10244")  # Default PIN
        return "10244"
    
    with open(PINCODE_FILE, "r") as file:
        return file.read().strip()


# PIN verification
def check_pin():
    correct_pin = load_pin()
    attempts = 3

    while attempts > 0:
        pin = input("Enter your PIN code: ")
        
        if pin == correct_pin:
            print("PIN is correct.\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN! Remaining attempts: {attempts}")

    print("ATM is locked after 3 incorrect attempts.")
    return False


# Load balance from file
def load_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "w") as file:
            file.write("0")
        return 0
    with open(BALANCE_FILE, "r") as file:
        return float(file.read())


# Save balance to file
def save_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))


# Check balance
def check_balance(balance):
    print(f"Your balance is: {balance} GEL")


# Deposit money
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Amount must be greater than 0!")
        return balance
    balance += amount
    print(f"Operation successful. {amount} GEL has been added to your account.")
    return balance


# Withdraw money
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Amount must be greater than 0!")
        return balance
    if amount > balance:
        print("Insufficient balance!")
        return balance
    balance -= amount
    print(f"Operation successful. {amount} GEL has been withdrawn from your account.")
    return balance


# ATM main menu
def atm():
    if not check_pin(): 
        return
    
    balance = load_balance()

    while True:
        print("\n--- ATM ---")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an operation (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance)
            save_balance(balance)

        elif choice == "3":
            balance = withdraw(balance)
            save_balance(balance)

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid operation! Try again.")


atm()